# Polybrutus D50 - exact 55-point labelled Euclidean metric

The **direct immutable scientific parent** is Topbrutus/polybrutus-d49@v0.1.0, actual tag commit \`3b7f96e2e89a5c0c7b0bd9ef8aa83fef1a72c9e0\`, DOI 10.5281/zenodo.24426743; its original complete ZIP SHA256 98504aea521ef2ccf250c67fdb20ad418ffeceac3df8cc8f6ab266802de18855, parent certificate SHA256 7541ceddea6b32419c6fc5dde7dbc0badbfc5c494bf8f17c5b73469e425d79e9.

## Construction and rank

Embed all 54 predecessor unit vectors p_i as q_i=(p_i,0), and add one perpendicular new unit vector q_55=e_51. All old labelled squared distances are conserved exactly; 54 new squared distances ||q_55-q_i||²=2R². C(55,2)=1485=1431+54.

The full exact rational Gram G is the orthogonal sum of a canonical seven-point rank-3 block, a five-point centered regular simplex rank-4 block (unit diagonal, mutual inner product -1/4), and 43 orthogonal independent unit axes. G=XXᵀ PSD rank 3+4+43=50. Set D_ij=2-2G_ij (i≠j), D_ii=0, H=I-11ᵀ/55; B=-HDH/2=HGH is PSD with rank 50. The origin is in the affine hull via the inherited antipodal canonical pair. Therefore minimum Euclidean affine rank 50; 51 coordinates stored.

Histogram k=4d²/R²: 4:6, 7:2, 8:1454, 9:3, 10:10, 12:6, 13:2, 16:2, 1485 pairs; sum at R=1: **11927/4**.

## Separate ideal weighted complete graph

For scalar unit masses and weights w_ij=1/d_ij², the added unit point contributes 54 new edges of weight 1/2. L50=[[L49+I54/2,-1_54/2],[-1_54ᵀ/2,27]]. Recurrence chi55(z)=z(z-55/2)chi54(z-1/2)/(z-1/2); chosen-model closed form chi55(z)=z(z-55/2)^44(z-27)^4*f6(z-24), where f6(z)=chiP7(z)/z is the 7-point model factor.

Exact Laplacian nullities establish eigenvalue 55/2 multiplicity 44 and eigenvalue 27 multiplicity 4. These are dimensionless model modes.

**Literature:** direct parent D49 DOI 10.5281/zenodo.24426743; historical D7 DOI 10.5281/zenodo.24407952. **Limits:** Only a synthetic exact Euclidean metric and a separately selected dimensionless ideal complete weighted graph are studied. No new physical dimensions, measured frequencies, particles, novel universal theorem or independent human peer review are established.
