a =: 1 2 3           NB. resultat: 1 2 3
b =: 1 1 1           NB. resultat: 1 1 1
c =: b + a           NB. resultat: 2 3 4

d =: 1 + a           NB. resultat: 2 3 4

e =: 1 1 + a         NB. length error

f =: 5 + 2 * 3       NB. resultat: 11
g =: 3 + 5 * 2       NB. resultat: 13
h =: (3 + 5) * 2     NB. resultat: 16

i =: _1 * 2 3        NB. resultat: [-2 -3]

a =: 5 - 2           NB. resultat: 3
b =: 2 * 3           NB. resultat: 6
c =: 6 % 2           NB. resultat: 3     NB. divisió real en J, però en G volem l'entera
d =: 2 | 7           NB. resultat: 1     NB. compte: els operands van al revés
e =: 2 ^ 3           NB. resultat: 8

r1 =: 3 > 2         NB. resultat: 1     
r2 =: 3 < 2         NB. resultat: 0     
r3 =: 3 >= 3        NB. resultat: 1
r4 =: 2 <= 1        NB. resultat: 0
r5 =: 4 = 4         NB. resultat: 1
r6 =: 5 <> 4        NB. resultat: 1
r7 =: 5 <> 5        NB. resultat: 0

a =: ~ 1             NB. resultat: 0
b =: ~ 0             NB. resultat: 1
c =: ~ 1 0 1         NB. resultat: 0 1 0

a =: 1 * 1           NB. resultat: 1
b =: 1 * 0           NB. resultat: 0
c =: 1 0 1 * 0 1 1   NB. resultat: 0 0 1

b =: 1 + 0           NB. resultat: 1
c =: 0 + 0           NB. resultat: 0
d =: 1 0 0 + 0 1 0   NB. resultat: 1 1 0
