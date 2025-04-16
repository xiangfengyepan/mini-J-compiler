a =: ] 1                    NB. results: 1
b =: 1 , 2 3                NB. results: 1 2 3
c =: # 1 2                  NB. results: 2
d =: 1 0 1 0 # 1 2 3 4      NB. results: 1 3
e =: 0 2 { 2 3 4            NB. results: 2 4
f =: i. 4                   NB. results: 0 1 2 3
g =: +: 1 2 3               NB. results: 2 4 6
h =: + / 1 2 3              NB. results: 6
i =: 7 | ~ 2                NB. results: 1

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