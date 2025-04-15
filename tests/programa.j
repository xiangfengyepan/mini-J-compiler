a =: 1 2 3           NB. results: 1 2 3
b =: 1 1 1           NB. results: 1 1 1
c =: b + a           NB. results: 2 3 4

d =: 1 + a           NB. results: 2 3 4

e =: 1 1 + a         NB. length error

f =: 5 + 2 * 3       NB. results: 11
g =: 3 + 5 * 2       NB. results: 13
h =: (3 + 5) * 2     NB. results: 16

i =: _1 * 2 3        NB. results: [-2 -3]

NB. print results
a
b
c 
d
e 
f 
g 
h
