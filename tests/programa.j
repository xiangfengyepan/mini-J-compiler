square =: *: ]
square 1 2 3 4    NB. resultat: 1 4 9 16

mod2 =: 2 | ]
mod2 i. 4    NB. resultat: 0 1 0 1

eq0 =: 0 = ]
eq0 mod2 i. 6    NB. resultat: 1 0 1 0 1 0

NB. parell =: eq0 @: mod2
NB. parell i. 6    NB. resultat: 1 0 1 0 1 0


