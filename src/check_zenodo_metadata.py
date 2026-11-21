#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'results/certificate_d50.json').read_text(encoding='utf8'))
m=json.loads((R/'publication/zenodo_metadata_blueprint.json').read_text(encoding='utf8'))
assert c['status']=='PASS'
assert c['dimension']==m['scientific_dimension']==50
assert c['vertices']==m['norm_one_vertices']==55
assert c['pairs']==m['exact_labelled_squared_pairs']==1485
assert c['affine_rank']==c['centered_gram_rank']==50
assert c['eigenvalue_55_over_2_multiplicity']==m['model_eigenvalue_55_over_2_multiplicity']==44
assert c['eigenvalue_27_multiplicity']==m['model_eigenvalue_27_multiplicity']==4
assert c['parent_tag_commit']=='3b7f96e2e89a5c0c7b0bd9ef8aa83fef1a72c9e0'
assert c['parent_doi']==m['scientific_parent_doi']=='10.5281/zenodo.24426743'
assert m['related_identifiers']==[{'identifier':'10.5281/zenodo.24426743','relation':'isDerivedFrom','resource_type':'publication-preprint','scheme':'doi'}]
assert len(m['keywords'])==9
assert 'affine Euclidean dimension fifty' in m['keywords']
assert 'forty-fourfold ideal eigenvalue' in m['keywords']
assert len(m['references'])==2
assert '10.5281/zenodo.24426743' in m['references'][0]
assert '10.5281/zenodo.24407952' in m['references'][1]
assert not any(x in str(m['keywords']) for x in ('forty-nine','forty-threefold','thirty-one','twenty-fivefold'))
doc=(R/'publication/POLYBRUTUS_50D_NOTE.md').read_text(encoding='utf8')
assert all(x in doc for x in ('## References','10.5281/zenodo.24426743','10.5281/zenodo.24407952'))
print('D50_ZENODO_CURRENT_METADATA_PARENT_DOI_AND_2_REFERENCES_PASS')
