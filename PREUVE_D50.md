# Polybrutus 50D - construction, independent verification and falsification

1. **Authentic frozen parent:** Git tag D49 v0.1.0 commit \`3b7f96e2e89a5c0c7b0bd9ef8aa83fef1a72c9e0\`, DOI 10.5281/zenodo.24426743. Original complete D49 ZIP, size 2681661 bytes, 33 entries, CRC PASS, SHA-256 98504aea521ef2ccf250c67fdb20ad418ffeceac3df8cc8f6ab266802de18855; its original certificate SHA-256 7541ceddea6b32419c6fc5dde7dbc0badbfc5c494bf8f17c5b73469e425d79e9. Both checkers validate archive, CRC and byte-identical parent certificate.
2. **Exact conservation:** embed all old 54 unit vertices in an extra zero coordinate and append a new perpendicular unit point. This preserves all 1431 old labelled squared distances exactly; 54 newly labelled squared distances equal 2R², yielding C(55,2)=1485.
3. **PSD Gram and minimum rank:** explicit rational Gram blocks rank 3+4+43=50 yield G=XXᵀ PSD. Its centered Euclidean B=-HDH/2=HGH PSD rank 50. Existing antipodal vertices ensure origin belongs to affine hull, hence minimum affine Euclidean dimension 50.
4. **Exhaustive count and sum:** class k=4d²/R² has counts 4:6, 7:2, 8:1454, 9:3, 10:10, 12:6, 13:2, 16:2. All 1485 labels verified; sum at R=1 is 11927/4. Inherited labelled pairs compared one-for-one to frozen D49 certificate.
5. **Independent ideal graph:** separate graph w_ij=1/d_ij², scalar unit masses; exact eigenvalue 55/2 multiplicity 44 and 27 multiplicity 4, independently computed rational nullities, no measured frequencies.
6. **Independent implementations:** src/verify_d50.py constructs a rational Gram; tests/independent_d50.py computes all distances with fractions.Fraction rules, no import of primary Gram program. Both regenerate the same deterministic certificate SHA256.
7. **Negative controls:** damaged pair, duplicated point, nonperpendicular norm-one rotated point with altered label, and a relabelling preserving only the histogram, each rejected in primary code (4/4). Independent checker independently rejects damaged label and histogram-preserving permutation.
8. **Bibliographic gate:** 9 current D50 keywords including \`fifty\`, \`forty-fourfold\`; structured \`isDerivedFrom\` to D49 DOI 10.5281/zenodo.24426743; separately \`references\` listing D49 parent and D7 historical 10.5281/zenodo.24407952. Public Zenodo readback required.

No experimental physics or independent peer review is claimed.
