NB. Operacions aritmètiques bàsiques
a =: 5 - 2          NB. result: 3
b =: 2 * 3          NB. result: 6
c =: 6 % 2          NB. result: 3
d =: 2 | 7          NB. result: 1
e =: 2 ^ 3          NB. result: 8

NB. Operacions amb vectors
f =: 1 1 1 + 1 2 3  NB. result: 2 3 4
g =: 1 + 1 2 3      NB. result: 2 3 4

NB. Operadors relacionals
h =: 3 > 2          NB. result: 1
i =: 3 < 2          NB. result: 0
j =: 3 >= 3         NB. result: 1
k =: 2 <= 1         NB. result: 0
l =: 2 = 2          NB. result: 1
m =: 2 <> 3         NB. result: 1

NB. Funcions especials
n =: ] 1 2 3        NB. result: 1 2 3
o =: 1 , 2 3        NB. result: 1 2 3
p =: # 1 2          NB. result: 2
q =: 1 0 1 0 # 1 2 3 4   NB. result: 1 3
r =: 0 2 { 2 3 4    NB. result: 2 4
s =: i. 4           NB. result: 0 1 2 3
t =: +: 1 2 3       NB. result: 2 4 6
u =: + / 1 2 3      NB. result: 6
v =: 7 | ~ 2        NB. result: 1

NB. Nombres negatius
w =: _1 * 2 3       NB. result: _2 _3

NB. Parèntesis per controlar prioritat
x =: 5 + 2 * 3      NB. result: 11
y =: (5 * 2) + 3    NB. result: 13
z =: 5 * 2 + 3      NB. result: 25

NB. Variables i operacions
foo =: 1 2 3
bar =: foo + 4      NB. result: 5 6 7

NB. Print results
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
w
x
y
z
foo
bar
