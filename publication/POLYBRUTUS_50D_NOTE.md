# Polybrutus 50D: Exact 55-point Euclidean metric and a forty-fourfold ideal graph mode

**Gabriel St-Pierre** - Independent researcher
**21 November 2026**
**Exact mathematical preprint / reproducible case study**
**AI assistance:** OpenAI ChatGPT (Astra) materially assisted exact rational analyses, separately implemented verifiers, manuscript and publication. AI is not a scientific author.

## Abstract

We provide one exact labelled squared-distance Euclidean metric on 55 norm-one points, created by appending a perpendicular unit vertex to the immutable Polybrutus 49D construction [1]. All 1431 predecessor labelled squared distances remain identical; exactly 54 new squared distances equal 2R², yielding 1485 unordered labelled pairs. The exact centered Gram is positive semidefinite rank 50, giving the minimum affine Euclidean embedding dimension of this synthetic metric. In a **separate stipulated** scalar-mass weighted complete graph with edge weights w_ij=1/d_ij², the ideal Laplacian has eigenvalue 55/2 with multiplicity 44 and eigenvalue 27 with multiplicity 4. Two independent rational programs validate all pair labels, parent source authenticity, centered ranks and spectral nullities. No physical dimensions or measured resonances are claimed.

## 1. Immutable scientific parent and labelled-distance conservation

Only direct scientific source is St-Pierre, Polybrutus 49D [1], DOI 10.5281/zenodo.24426743, Git tag v0.1.0 at actual frozen commit 3b7f96e2e89a5c0c7b0bd9ef8aa83fef1a72c9e0. The complete byte-identical original D49 source ZIP, including earlier nested archives, is stored at prior/d49/frozen_scientific_tag_v0.1.0.zip (2681661 bytes, 33 entries, CRC PASS, SHA-256 98504aea521ef2ccf250c67fdb20ad418ffeceac3df8cc8f6ab266802de18855). Original certificate prior/d49/results/certificate_d49.json, SHA-256 7541ceddea6b32419c6fc5dde7dbc0badbfc5c494bf8f17c5b73469e425d79e9, is copied without alteration. Both independent programs verify ZIP SHA/CRC and the original certificate bytes.

Zero-embed all old unit vectors p_i into the larger Euclidean coordinate space as q_i=(p_i,0), i=1,...,54. Add a new perpendicular unit vector q_55. Every predecessor squared distance, with its exact ordered pair of labels, remains unchanged. Each new squared distance is ||q_55-q_i||²=R²+R²-0=2R². Hence C(55,2)=1485=1431+54 unordered labelled pairs. This is a synthetic conservative Euclidean extension, not a claim of physical higher-dimensional spacetime.

## 2. Exact Gram rank and exhaustive rational histogram

The Gram G is a direct sum of the canonical seven norm-one points (rank three), a regular centered unit five-point simplex (rank four, off-diagonal inner product -1/4) and 43 orthogonal independent unit axes. Its exact rational unit-diagonal factorization G=XXᵀ gives positive semidefiniteness and rank 3+4+43=50. Write D_ii=0, D_ij=2-2G_ij, and H=I-11ᵀ/55. The centered Euclidean Gram B=-(1/2)HDH=HGH is positive semidefinite rank 50. The inherited canonical antipodal pair puts the origin inside the affine hull, so the minimal affine realization dimension is exactly 50; 51 coordinates are stored.

For R=1, normalized distance class k=4d²/R² has the exact histogram 4:6, 7:2, 8:1454, 9:3, 10:10, 12:6, 13:2, 16:2 (total 1485). The sum of all pairwise squared distances is 11927/4. The independent verifier compares every 1431 old labelled pair with the original frozen D49 certificate and regenerates all 1485 rational distances; histogram equality alone is insufficient for label preservation.

## 3. Chosen ideal graph and the spectral recurrence

Assign scalar unit masses and a dimensionless weight w_ij=1/d_ij² to each pair in the separately selected complete graph. The added point connects to every old vertex at weight 1/2. Its Laplacian is L50=[[L49+I54/2,-1_54/2],[-1_54ᵀ/2,27]]. Characteristic polynomial recurrence: chi55(z)=z(z-55/2)chi54(z-1/2)/(z-1/2). For the earlier seven-point factor f6(z)=chiP7(z)/z, the chosen-model expression is chi55(z)=z(z-55/2)^44(z-27)^4*f6(z-24).

Independent exact rational nullity checks give eigenvalue 55/2 multiplicity 44 and eigenvalue 27 multiplicity 4. They are mathematical model eigenmodes. Without separate physical assumptions and measurements, these are not values in hertz and do not establish particles, forces, physical spacetime dimensions or experimental resonance.

## 4. Independent implementations, falsification and provenance caveat

Primary src/verify_d50.py builds the Gram, 1485 exact labelled squared distances, full weighted Laplacian and centered Gram. tests/independent_d50.py independently regenerates rational distances using Python fractions.Fraction without importing the primary Gram generator; it independently recomputes the centered distance Gram and model Laplacian nullities. Both check authentic D49 source ZIP, CRC and certificate bytes, old pair labels, exact rank, histogram and model eigenvalue multiplicities. Both produce exactly the same SHA-256 of results/certificate_d50.json.

Four adversarial primary controls reject a damaged labelled pair, a duplicated last vertex, a unit-norm but nonorthogonally tilted new point, and an index permutation that preserves the distance histogram but changes labels. The independent program also rejects a damaged labelled pair and label permutation.

An inherited D47 source-certificate error labels its own D46 parent commit inaccurately; this was documented in the D48 release. D50 preserves every older source archive without rewriting historical bytes and authenticates its immediate D49 scientific parent tag independently.

## 5. Publication contract and scientific interpretation

Exact orthogonal Euclidean completion and weighted graph joins are established mathematical constructions. This work verifies one explicitly selected metric and a separately chosen graph, not a new universal mathematical theorem, a measured phenomenon or an independent human peer-reviewed result. Reproduction requires Python 3.12 and sympy==1.14.0.

For Zenodo, a structured isDerivedFrom relation must point to immediate D49 DOI 10.5281/zenodo.24426743, separate bibliography must include D49 [1] and historical D7 [2], and current keywords must include dimension fifty and ideal eigenvalue forty-fourfold. Each condition and all original file sizes/checksums must be confirmed through the published public Zenodo API.

## References

[1] St-Pierre, Gabriel (2026). Polybrutus 49D: Exact 54-Point Euclidean Metric and Forty-Threefold Ideal Graph Mode. Zenodo. DOI: 10.5281/zenodo.24426743. https://doi.org/10.5281/zenodo.24426743

[2] St-Pierre, Gabriel (2026). Polybrutus 7D: An Exact Twelve-Point Orthogonal Completion, the 12-35-37 Identity, and an Oscillator Model. Zenodo. DOI: 10.5281/zenodo.24407952. https://doi.org/10.5281/zenodo.24407952

[3] St-Pierre, Gabriel (2026). Polybrutus D49 frozen scientific tag v0.1.0, GitHub https://github.com/Topbrutus/polybrutus-d49/tree/v0.1.0, commit 3b7f96e2e89a5c0c7b0bd9ef8aa83fef1a72c9e0; full source ZIP embedded unchanged.
