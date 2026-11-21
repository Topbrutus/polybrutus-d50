#!/usr/bin/env python3
"""Polybrutus D50: exact Euclidean labelled metric and chosen ideal weighted graph.
Conservative perpendicular unit extension of the immutable Polybrutus D49 v0.1.0.
No physical spacetime dimension or experimentally measured resonance is claimed.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
from hashlib import sha256
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[1]
Q=s.Rational
core=[(0,0,1),(Q(1,2),0,Q(1,2)),(-Q(1,4),Q(3,4),Q(1,2)),
      (-Q(1,4),-Q(3,4),Q(1,2)),(0,0,-1),(Q(1,2),0,-Q(1,2)),
      (-Q(1,2),0,-Q(1,2))]
n=55
pairs=list(combinations(range(n),2))
G=s.zeros(n)
for i in range(7):
    for j in range(7):
        G[i,j]=3*core[i][0]*core[j][0]+core[i][1]*core[j][1]+core[i][2]*core[j][2]
for i in range(7,12):
    for j in range(7,12):
        G[i,j]=1 if i==j else -Q(1,4)
for i in range(12,n):
    G[i,i]=1
assert all(G[i,i]==1 for i in range(n))
assert DomainMatrix.from_Matrix(G).to_field().rank()==50
D=2*s.ones(n)-2*G
for i in range(n):
    D[i,i]=0
assert len(pairs)==1485 and all(D[i,j]>0 for i,j in pairs)

parent_path=ROOT/'prior'/'d49'/'results'/'certificate_d49.json'
parent_archive=ROOT/'prior'/'d49'/'frozen_scientific_tag_v0.1.0.zip'
assert sha256(parent_archive.read_bytes()).hexdigest()=='98504aea521ef2ccf250c67fdb20ad418ffeceac3df8cc8f6ab266802de18855'
from zipfile import ZipFile
with ZipFile(parent_archive) as _frozen:
    assert _frozen.testzip() is None
    assert _frozen.read('results/certificate_d49.json')==parent_path.read_bytes()
parent_bytes=parent_path.read_bytes()
assert sha256(parent_bytes).hexdigest()=='7541ceddea6b32419c6fc5dde7dbc0badbfc5c494bf8f17c5b73469e425d79e9'
parent=json.loads(parent_bytes)
assert parent['status']=='PASS' and parent['dimension']==49 and parent['vertices']==54
former={(int(e['i'])-1,int(e['j'])-1):s.Rational(e['d2'])
        for e in parent['labelled_squared_distances']}
assert len(former)==1431
assert all(D[i,j]==v for (i,j),v in former.items())
assert all(D[i,54]==2 for i in range(54))
hist=Counter(4*D[i,j] for i,j in pairs)
expected=Counter({4:6,7:2,8:1454,9:3,10:10,12:6,13:2,16:2})
assert hist==expected and sum(hist.values())==1485
assert sum(D[i,j] for i,j in pairs)==Q(11927,4)

H=s.eye(n)-s.ones(n)/n
B=-H*D*H/2
assert B==H*G*H
assert DomainMatrix.from_Matrix(B).to_field().rank()==50
# The first and fifth canonical points are antipodal; origin lies in the affine hull.
assert G[0,4]==-1

L=s.zeros(n)
for i,j in pairs:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
assert L*s.ones(n,1)==s.zeros(n,1)
assert DomainMatrix.from_Matrix(L-Q(55,2)*s.eye(n)).to_field().rank()==11
assert DomainMatrix.from_Matrix(L-27*s.eye(n)).to_field().rank()==51
old=s.zeros(54)
for i,j in combinations(range(54),2):
    w=1/D[i,j]
    old[i,i]+=w;old[j,j]+=w;old[i,j]-=w;old[j,i]-=w
assert L[:54,:54]-old==s.eye(54)/2
assert all(L[i,54]==-Q(1,2) for i in range(54))
assert L[54,54]==27

# Four adversarial negative controls.
damaged=D.copy();damaged[0,54]=damaged[54,0]=Q(9,4)
assert Counter(4*damaged[i,j] for i,j in pairs)!=hist
duplicate=G.copy();duplicate[54,:]=G[53,:];duplicate[:,54]=G[:,53];duplicate[54,54]=1
assert DomainMatrix.from_Matrix(duplicate).to_field().rank()==49
tilted_dot_to_old_core=Q(3,10)
assert Q(3,10)**2+Q(91,100)==1
assert tilted_dot_to_old_core!=0 and 2-2*tilted_dot_to_old_core!=D[0,54]
swapped=D.copy();swapped.row_swap(0,7);swapped.col_swap(0,7)
assert swapped!=D and Counter(4*swapped[i,j] for i,j in pairs)==hist

report={
  'schema':'POLYBRUTUS-D50-EXACT-CERTIFICATE-v1',
  'status':'PASS','dimension':50,'vertices':55,'pairs':1485,
  'affine_rank':50,'centered_gram_rank':50,'ambient_storage_coordinates':51,
  'radius':1,'parent':'Topbrutus/polybrutus-d49@v0.1.0',
  'parent_tag_commit':'3b7f96e2e89a5c0c7b0bd9ef8aa83fef1a72c9e0',
  'parent_doi':'10.5281/zenodo.24426743',
  'parent_certificate_sha256':sha256(parent_bytes).hexdigest(),
  'parent_frozen_tag_archive_sha256':sha256(parent_archive.read_bytes()).hexdigest(),
  'parent_frozen_tag_embedded_as_verified_zip':True,
  'parent_distances_preserved':1431,'new_distances':54,
  'new_squared_distances':['2']*54,
  'histogram_k_4d2':{str(k):int(v) for k,v in sorted(hist.items())},
  'sum_squared_distances':'11927/4',
  'gram_psd_certificate':'B=-(H D H)/2=H G H; G=XX^T exact',
  'negative_controls':'4/4 PASS',
  'oscillator_model':'Chosen ideal equal-mass complete graph with w_ij=1/d_ij^2; no physical measurement',
  'eigenvalue_55_over_2_multiplicity':44,
  'eigenvalue_27_multiplicity':4,
  'spectral_recurrence':'chi55(z)=z*(z-55/2)*chi54(z-1/2)/(z-1/2)',
  'spectral_closed_form':'chi55(z)=z*(z-55/2)^44*(z-27)^4*f6(z-24), f6(z)=chiP7(z)/z',
  'novel_universal_theorem':'NOT CLAIMED','physical_discovery':'NOT CLAIMED',
  'human_peer_review':'NOT_DONE','sympy':s.__version__,
  'labelled_squared_distances':[{'i':i+1,'j':j+1,'d2':str(D[i,j]),'k':str(4*D[i,j])} for i,j in pairs]
}
out=ROOT/'results'/'certificate_d50.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
print('PRIMARY D50 PASS: 55 vertices, 1485 labelled pairs, affine rank 50; 1431/1431 previous pairs preserved')
print('IDEAL GRAPH PASS: eigenvalue 55/2 x44; eigenvalue 27 x4; 4/4 negative controls')
print('CERTIFICATE_SHA256='+sha256(out.read_bytes()).hexdigest())
