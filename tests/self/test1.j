NB. Identitat
] 1 _2 3

NB. Concatenacio
_1 , ] 2 3

NB. Mida
# _1 , ] 2 3

1 0 1 0 # 1 2 , 3 4

0 2 { _1 , 1 2 3

i. # 1 2 3 4 

*: 1 2 3
*: 3 2 1

* / 1 2 3
NB. % / 12 2 3
NB. ^ / 1 2 3
NB. | / 3 2
NB. - / 1 2 3

7 | ~ 2
7 - ~ 2
2 % ~ 8 
_1 , 1 2 3 { ~ 0 2
_1 , ~ 2 3


square =: *:
square 1 + i. 3    NB. resultat: 1 4 9

mod2 =: 2 | ]
eq0 =: 0 = ]

eq0 mod2 i. 6    NB. resultat: 1 0 1 0 1 0

parell =: eq0 @: mod2
parell i. 6    NB. resultat: 1 0 1 0 1 0

parell =: 0 = ] @: 2 | ]
parell i. 6    NB. resultat: 1 0 1 0 1 0

inc =: 1 + ]
test =: +/ @: inc @: i.
test 3    NB. resultat: 6


