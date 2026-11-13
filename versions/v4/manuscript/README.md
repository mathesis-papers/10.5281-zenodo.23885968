# OEIS A391810: formula (5), COMMENTS (C.1)--(C.10), and prime-index vanishing

Revision 4, 2 November 2026. Haobo Ma (ChronoAI Pte Ltd, Singapore),
then Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore).
CC BY 4.0 (`cc-by-4.0`). Third-party snapshots retain their original terms:
OEIS materials follow the OEIS End-User License Agreement; the Lean sources
retain `sources/UPSTREAM-LICENSE`.

## Rebuild

From this directory, use Python 3 and Tectonic 0.17.0:

```sh
python3 verify.py --output verification.json
tectonic note.tex
```

Alternatively, run `pdflatex note.tex` twice. The bibliography is in `note.tex`;
BibTeX and external figures are unnecessary. The readable PDF accompanies
the archive. `source-manifest.json` gives sizes and SHA256 hashes of every
other archive member.

## Results

For n>=1, the original Laurent coefficients equal coefficients of
`P_n(y)=-1+sum(h=1..n)y^h(1-y^h)^(n-h)`, of degree at most
`B_n=floor((n+1)/2)^2`. Thus `T(n,0)=-1`, and for k>=1,

`T(n,k)=sum(h|k, 1<=h<=n) (-1)^(k/h-1) binom(n-h,k/h-1)`.

Binomial coefficients outside their ordinary range equal zero. This gives
the small-column, edge-coefficient and prime-index formulas of COMMENTS.
The complete written proofs retain the inclusive row endpoint and the
exceptional constant from the bilateral series.

| A391810 revision 39 locator | Coverage | Registered problem ID |
| --- | --- | --- |
| Formula (1), endpoint | Definition and Lemma 1 | Same row model |
| Formula (5) | Theorem 1: negative alternating sum = 2 round(2^n/3) = 2J_n | oeis-a391810-alternating-jacobsthal |
| Formula (2); row-sum COMMENT | Corollary 5: row sum zero | oeis-a391810-full-laurent-row-sums |
| Formula (3) | Corollary 5: first moment one | oeis-a391810-laurent-first-moment |
| Formula (4) | Corollary 5: second moment 5-2n for n>=2 | oeis-a391810-second-moment |
| Formula (6) | Corollary 6: alternating first-moment generating function | Source locator |
| COMMENTS (C.1)--(C.5) | Corollaries 1--2: divisor formula and small columns | Source locators |
| COMMENTS (C.6)--(C.9) | Corollary 3: leading and adjacent coefficients | Source locators |
| COMMENT (C.10) | Corollary 4: T(p,p)=2 for odd primes | Source locator |
| COMMENT (C.11), zero clause | Corollary 4: T(n,q)=0 for every prime q>n | Source locator |
| COMMENT (C.11), first zero | Open here; agrees with rows 5--79 | Source locator |
| Formula (7); A391811 | Defining relation; positive integrality from the row sum | Source locators |
| Two related bilateral identities in COMMENTS | Outside these nonpositive-coefficient results | Source locators |

`coverage.json` records the exact source quotes and proof locations. The four
registered problem IDs in `metadata.json` retain their identities; the other
consequences use the precise OEIS source locators.

## Verification scope

`verify.py` uses Python integers and rational numbers to compare the polynomial,
the divisor formula and an independent expansion of the original Laurent terms
for every k=0,...,B_n+5 in rows 1--79. It checks all 94 displayed sequence terms,
COMMENTS (C.1)--(C.10) on applicable rows, prime zeros for n<q<=2n+17,
the first-zero observation in rows 5--79, all four moment identities on rows
1--79, and the Jacobsthal scalar identity through n=512. Formula (6) is checked
by a separate rational-series convolution. Finite checks supplement the
universal written proofs; they do not settle the first-zero assertion.
The positive integral half-squared norms match all 28 displayed A391811 terms.

The four Lean modules are source snapshots at Trureturing commit
`1239bd2a0ed6e9d54aabb5a42af94234e9eb61ae`:

- `HannaLaurentAlternatingJacobsthal.full_formula_five`: formula (5), rounding,
  the original-Laurent coefficient bridge and support.
- `HannaLaurentRowSums.series_coefficient`, `row_degree`, `result`: the bridge,
  support and formula (2).
- `HannaLaurentFirstMoment.result`: formula (3).
- `HannaLaurentSecondMoment.result`: formula (4).

The PDF body links each pinned module. Formula (6), the divisor formula,
COMMENTS (C.1)--(C.10), and prime-index vanishing have written proofs in the note.
The included modules are snapshots rather than a standalone Lean project.
