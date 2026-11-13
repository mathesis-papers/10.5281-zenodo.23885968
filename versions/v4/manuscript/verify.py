import argparse
from fractions import Fraction
import hashlib
import json
from math import comb, isqrt
from pathlib import Path


def generalized_binomial(upper, lower):
    if upper >= 0:
        return comb(upper, lower) if lower <= upper else 0
    return (-1) ** lower * comb(lower - upper - 1, lower)


def finite_polynomial(row):
    coefficients = {0: -1}
    for index in range(1, row + 1):
        for power in range(row - index + 1):
            degree = index * (power + 1)
            coefficients[degree] = coefficients.get(degree, 0) + (-1) ** power * comb(row - index, power)
    return {degree: value for degree, value in coefficients.items() if value}


def original_laurent_coefficient(row, degree):
    total = 0
    for outer in range(-(2 * row + 7), 8):
        if outer == 0:
            continue
        exponent = row + outer
        if outer > 0:
            order = outer
            step = outer
            prefactor = 1
        else:
            step = -outer
            order = step * (step - row - 1)
            prefactor = -1 if exponent % 2 else 1
        difference = degree - order
        if difference >= 0 and difference % step == 0:
            power = difference // step
            total += prefactor * (-1) ** power * generalized_binomial(exponent, power)
    return total


def nearest_integer(value):
    return (2 * value.numerator + value.denominator) // (2 * value.denominator)


def alternating_moment_from_rational_series(row):
    numerator = {1: 1, 2: -1, 3: 8}
    return sum(weight * sum((-1) ** first * (first + 1) *
               (row - shift - first + 1) * 2 ** (row - shift - first)
               for first in range(row - shift + 1))
               for shift, weight in numerator.items() if shift <= row)


def divisor_coefficient(row, index):
    if index == 0:
        return -1
    total = 0
    for divisor in range(1, min(row, index) + 1):
        if index % divisor == 0:
            power = index // divisor - 1
            if power <= row - divisor:
                total += (-1) ** power * comb(row - divisor, power)
    return total


def is_prime(number):
    return number >= 2 and all(number % divisor for divisor in range(2, isqrt(number) + 1))


def run():
    jacobsthal = [0, 1]
    for index in range(2, 513):
        jacobsthal.append(jacobsthal[-1] + 2 * jacobsthal[-2])
    coefficient_checks = 0
    divisor_checks = 0
    term_checks = {f"C.{index}": 0 for index in range(1, 12)}
    prime_zero_checks = 0
    first_zero_rows = []
    rows = []
    observed_flattening = []
    half_squared_norms = []
    for row in range(1, 80):
        polynomial = finite_polynomial(row)
        bound = ((row + 1) // 2) ** 2
        assert max(polynomial) <= bound
        for index in range(bound + 6):
            assert polynomial.get(index, 0) == original_laurent_coefficient(row, -index)
            coefficient_checks += 1
            assert polynomial.get(index, 0) == divisor_coefficient(row, index)
            divisor_checks += 1
        alternating = -sum((-1) ** degree * value for degree, value in polynomial.items())
        rounded = nearest_integer(Fraction(2 ** row, 3))
        assert alternating == 2 * rounded == 2 * jacobsthal[row]
        assert polynomial[0] == -1
        row_sum = sum(polynomial.values())
        first_moment = sum(degree * value for degree, value in polynomial.items())
        second_moment = sum(degree ** 2 * value for degree, value in polynomial.items())
        alternating_moment = -sum((-1) ** degree * degree * value
                                  for degree, value in polynomial.items())
        assert row_sum == 0
        assert first_moment == 1
        assert second_moment == (1 if row == 1 else 5 - 2 * row)
        assert alternating_moment == alternating_moment_from_rational_series(row)
        squared_norm = sum(value * value for value in polynomial.values())
        assert squared_norm % 2 == 0 and squared_norm >= 2
        half_squared_norms.append(squared_norm // 2)
        small_terms = {0: -1, 1: 1}
        if row >= 2:
            small_terms[2] = -(row - 2)
        if row >= 3:
            small_terms[3] = row * (row - 3) // 2 + 2
        if row >= 4:
            small_terms[4] = -(row - 3) * (row * row - 3 * row + 8) // 6
        for index, expected in small_terms.items():
            assert polynomial.get(index, 0) == expected
            term_checks[f"C.{index + 1}"] += 1
        middle = (row + 1) // 2
        if row % 2:
            assert polynomial.get(middle * middle, 0) == (-1) ** (middle - 1)
            term_checks['C.6'] += 1
            if middle >= 2:
                assert polynomial.get(middle * middle - 1, 0) == 2 * (-1) ** middle
                term_checks['C.7'] += 1
        else:
            assert polynomial.get(middle * middle, 0) == middle * (-1) ** (middle - 1)
            term_checks['C.8'] += 1
            if middle >= 2:
                assert polynomial.get(middle * middle - 1, 0) == 2 * middle * (-1) ** middle
                term_checks['C.9'] += 1
        if row % 2 and is_prime(row):
            assert polynomial.get(row, 0) == 2
            term_checks['C.10'] += 1
        for prime in range(row + 1, 2 * row + 18):
            if is_prime(prime):
                assert polynomial.get(prime, 0) == divisor_coefficient(row, prime) == 0
                prime_zero_checks += 1
        if row >= 5:
            next_prime = next(candidate for candidate in range(row + 1, 2 * row + 18) if is_prime(candidate))
            assert next_prime <= bound
            first_zero = next(index for index in range(bound + 1) if polynomial.get(index, 0) == 0)
            assert first_zero == next_prime
            term_checks['C.11'] += 1
            first_zero_rows.append({'n': row, 'first_zero': first_zero, 'next_prime': next_prime})
        if row <= 9:
            observed_flattening.extend(polynomial.get(index, 0) for index in range(bound + 1))
        rows.append({"n": row, "bound": bound, "degree": max(polynomial),
                     "alternating_sum": alternating, "row_sum": row_sum,
                     "first_moment": first_moment, "second_moment": second_moment,
                     "alternating_first_moment": alternating_moment})
    for row in range(1, 513):
        value = -1 - sum(2 ** (row - index) for index in range(1, row + 1, 2))
        if row % 2 == 0:
            value += 1
        assert -value == 2 * jacobsthal[row]
        assert 3 * jacobsthal[row] == 2 ** row - (-1) ** row
        assert nearest_integer(Fraction(2 ** row, 3)) == jacobsthal[row]
        assert abs(Fraction(2 ** row, 3) - jacobsthal[row]) == Fraction(1, 3)
    assert nearest_integer(Fraction(1, 2)) == 1
    assert nearest_integer(Fraction(-1, 2)) == 0
    assert nearest_integer(Fraction(3, 2)) == 2
    assert -sum(value * (-1) ** degree for degree, value in finite_polynomial(0).items()) == 1
    assert 2 * jacobsthal[0] == 0
    assert -sum(value * (-1) ** degree for degree, value in finite_polynomial(1).items()) == 2
    assert -sum(value * (-1) ** degree for degree, value in finite_polynomial(2).items()) == 2
    assert [item['alternating_first_moment'] for item in rows[:8]] == [1, 1, 13, 25, 81, 181, 453, 1025]
    source = Path(__file__).parent / "sources/A391810.seq"
    primary_match = None
    if source.is_file():
        terms = []
        for line in source.read_text().splitlines():
            if line.startswith(("%S A391810 ", "%T A391810 ", "%U A391810 ")):
                terms.extend(int(term) for term in line.split(" ", 2)[2].strip(",").split(","))
        assert observed_flattening[:len(terms)] == terms
        primary_match = len(terms)
    norm_source = Path(__file__).parent / "sources/A391811.seq"
    norm_terms = []
    for line in norm_source.read_text().splitlines():
        if line.startswith(("%S A391811 ", "%T A391811 ", "%U A391811 ")):
            norm_terms.extend(int(term) for term in line.split(" ", 2)[2].strip(",").split(","))
    assert half_squared_norms[:len(norm_terms)] == norm_terms
    return {
        "status": "passed",
        "arithmetic": "Python integers and fractions.Fraction; no floating point",
        "full_rows": [1, 79],
        "coefficient_comparisons": coefficient_checks,
        "divisor_formula_comparisons": divisor_checks,
        "coefficient_scope": "k=0 through B_n+5, with literal summands normalized independently of finite_polynomial",
        "outer_index_scope": "j=-(2n+7) through 7; the written valuation proof excludes every omitted contributor for tested nonpositive exponents",
        "scalar_rows": [1, 512],
        "primary_sequence_terms_matched": primary_match,
        "companion_A391811_terms_matched": len(norm_terms),
        "positive_integral_half_squared_norm_rows": [1, 79],
        "sibling_formulas_checked": {
            "formula_2": {"rows": [1, 79], "expected": "row sum = 0"},
            "formula_3": {"rows": [1, 79], "expected": "first moment = 1"},
            "formula_4": {"rows": [2, 79], "expected": "second moment = 5-2n", "excluded_n1_value": 1},
            "formula_6": {"rows": [1, 79], "expected": "coefficients of z(1-z+8z^2)/((1+z)^2(1-2z)^2)",
                          "independent_method": "direct convolution of (1+z)^(-2) and (1-2z)^(-2), not the derivative parity proof"}
        },
        "boundary_tests": ["n=1", "n=2 even boundary cancellation", "n=0 finite-polynomial non-extension", "exact half-integer rounding convention"],
        "first_six": [item["alternating_sum"] for item in rows[:6]],
        "rows": rows,
        "comment_formula_checks": term_checks,
        "prime_zero_checks": {"count": prime_zero_checks, "row_range": [1, 79], "prime_range_per_row": "n < q <= 2n+17"},
        "first_zero_observations": {"row_range": [5, 79], "universal_statement": "open in this note", "rows": first_zero_rows},
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_limit": "Finite checks supplement the written proofs. The first-zero observations cover rows 5 through 79; prime-index vanishing has a universal written proof.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2) + "\n"
    if arguments.output:
        arguments.output.write_text(text)
    print(json.dumps({key: value for key, value in result.items() if key != "rows"}, indent=2))


if __name__ == "__main__":
    main()
