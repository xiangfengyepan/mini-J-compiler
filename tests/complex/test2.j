NB. Operaciones combinadas complejas
a =: (1 2 3 + 4 5 6) * 2     NB. results: 10 14 18 (Suma de dos listas, luego multiplicación por 2)
b =: (6 7 8 * 2 2 2) + 10    NB. results: 22 24 26 (Multiplicación de listas, luego suma de 10)
c =: (3 6 9 + 1 1 1) * (2 2 2) NB. results: 8 14 20 (Suma de listas, luego multiplicación por una lista)
d =: (5 4 3 * 2 3 4) - (10 9 8) NB. results: 0 3 4 (Multiplicación de listas, luego resta de otra lista)

NB. Operaciones con adverbios y listas
e =: +/ (2 4 6 8) * 3       NB. results: 60 (Multiplicación de lista por 3, luego suma de los elementos)
f =: * / 2 4 6 8           NB. results: 384 (Producto total de los elementos)
g =: (2 3 4 + 1 1 1) * 3    NB. results: 9 12 15 (Suma de listas, luego multiplicación por un escalar)

NB. Operaciones con listas de diferentes tamaños
h =: 3 6 9 + 1 2 3 4         NB. results: error (listas de diferente tamaño)
i =: (3 6 9) * 1 2 3         NB. results: 3 12 27 (Multiplicación de listas de diferente tamaño)
j =: 10 + 1 2 3 4            NB. results: 11 12 13 14 (Suma de un escalar con una lista)

NB. Operaciones con relaciones entre listas
k =: (1 2 3 4) < 5 6 7 8      NB. results: 1 1 1 1 (Comparación de cada elemento con otro)
l =: 5 = 5 5 5                NB. results: 1 1 1 (Igualdad entre valor escalar y lista)
m =: 7 > 5 4 3                NB. results: 1 1 1 (Comparación mayor que con un escalar y lista)
n =: (2 4 6) <> 3 5 6         NB. results: 1 1 0 (Comparación diferente entre listas)

NB. Operaciones combinadas con adverbios
o =: (2 4 6 + 5 5 5) * 3       NB. results: 21 27 33 (Suma de listas, luego multiplicación por 3)
p =: +/ (1 1 1) * (2 3 4)     NB. results: 9 (Suma de la lista de 1, luego multiplicación por otra lista)

NB. Combinación de multiplicación, adverbios y relaciones
q =: 2 * +/ 3 6 9             NB. results: 36 (Multiplicación de escalar por la suma de una lista)
r =: (2 3 4) * (1 2 3) + 5    NB. results: 12 21 32 (Multiplicación de listas, luego suma de un escalar)
s =: 6 6 6 > 5 5 5           NB. results: 1 1 1 (Comparación mayor que entre listas)

NB. Operaciones combinadas avanzadas con adverbios
t =: (2 4 6 + 1 2 3) * +/ 1 1 1   NB. results: 9 18 27 (Suma de listas, luego multiplicación por adverbio)
u =: (5 10 15) + 2 * +/ 3 4 5     NB. results: 29 34 39 (Multiplicación y suma con adverbio)
v =: (7 8 9) * +/ (1 2 3)        NB. results: 42 48 54 (Multiplicación por la suma de la lista)

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
s
t
u
v
