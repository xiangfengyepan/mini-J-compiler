NB. Test de precedencia aritmética
a =: 2 + 3 * 4              NB. results: 14        (Multiplicación antes que suma: 2 + (3 * 4))
b =: (2 + 3) * 4            NB. results: 20        (Paréntesis fuerzan precedencia: (2 + 3) * 4)
c =: 2 * 3 ^ 2              NB. results: 18        (Potencia antes que multiplicación: 2 * (3 ^ 2))
d =: 2 ^ 3 * 2              NB. results: 64        ((2 ^ 3) * 2)

NB. Test con operadores especiales y precedencia
e =: 1 2 3 + 4 5 6 , 7 8 9  NB. results: 5 7 9 7 8 9 (Suma primero, luego concatenación)
f =: 2 4 6 { 0 1 2 + 1 1 1  NB. results: 4 6        (Suma primero, luego indexación)
g =: 1 2 3 , 4 5 6 + 1 1 1  NB. results: 1 2 3 5 6 7 (Suma primero, luego concatenación)

NB. Test con adverbios
h =: +/ 2 4 6 * 3           NB. results: 36        (Multiplicación primero, luego suma: +/ (6 12 18))
i =: +/ 2 4 6 + 1 1 1       NB. results: 15        (Suma de listas, luego adverbio suma total)
j =: * / 2 4 6             NB. results: 48         (Producto total: 2 * 4 * 6)

NB. Test con comparaciones y aritmética
k =: 2 + 3 * 4 = 14         NB. results: 1         ((2 + 12) = 14 → 1)
l =: 2 + 3 = 5             NB. results: 1         ((2 + 3) = 5 → 1)
m =: 3 * 3 = 9             NB. results: 1         ((3 * 3) = 9 → 1)

NB. Test combinado
n =: (1 2 3 + 4 5 6) * +/ 1 1 1   NB. results: 18 24 30 (Suma de listas, multiplicado por suma total)
o =: (5 10 15) + 2 * +/ 3 4 5     NB. results: 29 34 39 (Suma lista con 2 * suma de otra lista)
p =: 7 8 9 * +/ (1 2 3)           NB. results: 42 48 54 (Multiplicación por suma de lista)

NB. Comparaciones avanzadas
q =: 3 6 9 = 3 6 9               NB. results: 1 1 1
r =: 3 6 9 > 2 6 10              NB. results: 1 0 0
NB. s =: (1 2 3) <=/ (1 2 4)              NB. results: 1 1 1

NB. Imprimir resultados
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
NB. s
