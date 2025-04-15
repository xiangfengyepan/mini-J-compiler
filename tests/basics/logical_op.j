a =: ~ 1             NB. results: 0
b =: ~ 0             NB. results: 1
c =: ~ 1 0 1         NB. results: 0 1 0

d =: 1 * 1           NB. results: 1
e =: 1 * 0           NB. results: 0
f =: 1 0 1 * 0 1 1   NB. results: 0 0 1

g =: 1 + 0           NB. results: 1
h =: 0 + 0           NB. results: 0
i =: 1 0 0 + 0 1 0   NB. results: 1 1 0

NB. print results
a
b
c 
d
e 
f 
g 
h
i
