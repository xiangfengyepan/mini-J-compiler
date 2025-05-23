] 1 _2 3                    NB. 1 _2 3
1 , ] _2 3                  NB. 1 _2 3
# _1 , ] 2 3                NB. 3


NB. Mascara a # b
NB. Pre: len(a) == len(b)
NB. Pos: filtre amb mascara per tots el valor 0, si es diferent a 0 no el elimina
1 0 1 0 # 1 2 , 3 4         NB. 1 3
NB. 1 0 1 _1 # 1 2 , 3 4    NB. 1 3 4
NB. 1 0 1 5 # 1 2 , 3 4     NB. 1 3 4
1 0 1  # 1 2 , 3 4          NB. error length


0 2 { _1 , 1 2 3            NB. _1 2
_1 _2 { _1 , 1 2 3          NB. 3 2
4 { _1 , 1 2 3              NB. error index


i. # 99 100 1 2             NB. i. (4) = 0 1 2 3
NB. i. 1 2                  NB. errr length


*: 1 2 3                    NB. 1 2 3 * 1 2 3 = 1 4 9 
NB. ^: 1 2 3                NB. 1 2 3 ^ 1 2 3 = 1 4 27
NB. ,: 1 2 3                NB. 1 2 3 , 1 2 3 = 1 2 3 1 2 3


* / 1 2 3                   NB. (1 * 2) * 3 = 6
NB. % / 12 2 3              NB. (12 % 2) % 3 = 2
NB. ^ / 2 3 4               NB. (2 ^ 3) ^ 4 = 4096
NB. | / 7 4 2               NB. (7 mod 4) mod 2 = 1  
NB. - / 1 2 3               NB. (1 - 2) - 3 = _4  

7 | ~ 2                     NB. 7 mod 2 = 1
7 - ~ 2                     NB. 2 - 7 = _5
2 % ~ 8                     NB. 8 / 2 = 4
_1 , 1 2 3 { ~ 0 2          NB. _1 (0 2 { 1 2 3)  = _1 1 3
_1 , ~ 2 3                  NB. 2 3 , _1 = 2 3 _1

mod5 =: 5 | ]
eq0 =: 0 = ]
inc =: 1 + ]
mul5 =: eq0 @: mod5            

allMul5_from_1_100 =: (mul5 inc i.100) # inc i.100
allMul5_from_1_100
