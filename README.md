# OEIS A391810: formula (5), COMMENTS (C.1)--(C.10), and prime-index vanishing

**Authors:** Haobo Ma, Wenlin Zhang

We prove formula (5), COMMENTS (C.1)--(C.10), and the zero clause of COMMENT (C.11) of Paul D. Hanna's OEIS entry A391810, revision 39. For n>=1, the original bilateral Laurent coefficients form a finite row polynomial P_n(y)=-1+sum(h=1..n)y^h(1-y^h)^(n-h). Evaluating it at -1 gives the negative alternating row sum 2 round(2^n/3)=2J_n. The same polynomial proves formulas (2), (3), (4), and (6). Its divisor-sum coefficient expression proves the ten individual-term formulas and T(n,q)=0 for every prime q>n. The further first-zero assertion of (C.11) remains open in this note.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.23885969](https://doi.org/10.5281/zenodo.23885969)
- Concept DOI: [https://doi.org/10.5281/zenodo.23885968](https://doi.org/10.5281/zenodo.23885968)
- License: CC-BY-4.0
- Version: 4
- Mathesis record: [oeis-a391810-alternating-jacobsthal](https://mathesis-omega-research.apps.chrono-ai.fun/papers/oeis-a391810-alternating-jacobsthal?version=4)

## How to cite

Haobo Ma, Wenlin Zhang (2026). OEIS A391810: formula (5), COMMENTS (C.1)--(C.10), and prime-index vanishing. Mathesis, version 4. https://doi.org/10.5281/zenodo.23885969

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/1239bd2a0ed6e9d54aabb5a42af94234e9eb61ae/D5/S3/ArithSums/HannaLaurentAlternatingJacobsthal.lean#L103) | No public receipt |
| Lemma (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/1239bd2a0ed6e9d54aabb5a42af94234e9eb61ae/D5/S3/ArithSums/HannaLaurentAlternatingJacobsthal.lean#L103) | No public receipt |
| Corollary (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/1239bd2a0ed6e9d54aabb5a42af94234e9eb61ae/D5/S3/ArithSums/HannaLaurentAlternatingJacobsthal.lean#L103) | No public receipt |
| Corollary (s4) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/1239bd2a0ed6e9d54aabb5a42af94234e9eb61ae/D5/S3/ArithSums/HannaLaurentAlternatingJacobsthal.lean#L103) | No public receipt |
| Corollary (s5) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/1239bd2a0ed6e9d54aabb5a42af94234e9eb61ae/D5/S3/ArithSums/HannaLaurentAlternatingJacobsthal.lean#L103) | No public receipt |
| Corollary (s6) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/1239bd2a0ed6e9d54aabb5a42af94234e9eb61ae/D5/S3/ArithSums/HannaLaurentAlternatingJacobsthal.lean#L103) | No public receipt |
| Corollary (s7) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/1239bd2a0ed6e9d54aabb5a42af94234e9eb61ae/D5/S3/ArithSums/HannaLaurentAlternatingJacobsthal.lean#L103) | No public receipt |
| Corollary (s8) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/1239bd2a0ed6e9d54aabb5a42af94234e9eb61ae/D5/S3/ArithSums/HannaLaurentAlternatingJacobsthal.lean#L103) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).
