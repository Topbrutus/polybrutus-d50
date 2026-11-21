# Polybrutus 50D - exact 55-point Euclidean metric and forty-fourfold ideal graph mode

**Human scientific author:** Gabriel St-Pierre, independent researcher.
**Material AI assistance:** OpenAI ChatGPT (Astra) assisted two verifiers, exact rational checks, manuscript and publication; AI is not the author.

## Verified exact mathematical construction

- **55** norm-one vertices and **1485 / 1485** exact labelled unordered squared-distance pairs.
- All **1431 / 1431** labelled distances of immutable predecessor D49 are preserved; **54** new squared distances exactly **2R²**.
- Gram and centered Gram PSD with exact rank **50**, proving minimum affine Euclidean realization dimension 50 for this synthetic metric (51 coordinate storage).
- Exact class histogram k=4d²/R²: 4:6, 7:2, 8:1454, 9:3, 10:10, 12:6, 13:2, 16:2. At unit radius, exact squared-distance sum **11927/4**.
- A separately stipulated ideal complete graph with scalar unit masses and edges w_ij=R²/d_ij² has eigenvalue **55/2 multiplicity 44** and **27 multiplicity 4** (dimensionless graph modes, not measured hertz).
- Primary rational Gram program and independently written fractions.Fraction rule checker; four primary negative controls detect erroneous pair, duplicated vertex, nonorthogonal new point, and histogram-preserving relabelling.

## Run the independent proofs

    python -m pip install sympy==1.14.0
    python src/verify_d50.py
    python tests/independent_d50.py
    python src/check_zenodo_metadata.py

Both verifiers independently reproduce the deterministic SHA256 of \`results/certificate_d50.json\`. GitHub CI reruns them and verifies current metadata.

## Frozen direct ancestry and bibliographic controls

**Only direct scientific parent:** [Polybrutus 49D scientific v0.1.0](https://github.com/Topbrutus/polybrutus-d49/tree/v0.1.0), immutable Git tag commit \`3b7f96e2e89a5c0c7b0bd9ef8aa83fef1a72c9e0\`, DOI [10.5281/zenodo.24426743](https://doi.org/10.5281/zenodo.24426743), parent certificate SHA-256 \`7541ceddea6b32419c6fc5dde7dbc0badbfc5c494bf8f17c5b73469e425d79e9\`.

Original full parent ZIP (including nested older source archives) is embedded unchanged at \`prior/d49/frozen_scientific_tag_v0.1.0.zip\` SHA256 \`98504aea521ef2ccf250c67fdb20ad418ffeceac3df8cc8f6ab266802de18855\`; the original parent certificate is copied byte-identically and both verifiers authenticate original hashes and CRC.

Zenodo metadata must use dimension **fifty** and mode multiplicity **forty-fourfold**, a structured \`isDerivedFrom\` relation to the direct D49 DOI, and a distinct \`references\` list citing D49 and historical D7. Public API verification is mandatory after publication.

[Specification](SPECIFICATION_D50.md) | [proof](PREUVE_D50.md) | [provenance](PROVENANCE.md) | [references](REFERENCES.md) | [scientific PDF](publication/POLYBRUTUS_50D_NOTE.pdf).

**Scope:** Only a synthetic exact Euclidean metric and a separately selected dimensionless ideal complete weighted graph are studied. No new physical dimensions, measured frequencies, particles, novel universal theorem or independent human peer review are established.
**Licensing:** MIT source, CC BY 4.0 manuscript.
