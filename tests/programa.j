square =: *: ]
square 1 2 3 4    NB. resultat: 1 4 9 16

mod2 =: 2 | ]
mod2 i. 4    NB. resultat: 0 1 0 1

eq0 =: 0 = ]
eq0 mod2 i. 6    NB. resultat: 1 0 1 0 1 0

parell =: 0 = ] @: 2 | ]
parell i. 6    NB. resultat: 1 0 1 0 1 0


inc =: 1 + ]
test =: +/ @: 1 + ] @: i.
test 3    NB. resultat: 6

