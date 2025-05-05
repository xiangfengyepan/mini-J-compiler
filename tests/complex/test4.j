NB. Asignación de operadores a variables
identity =: ]        NB. `identity` se asigna al operador de identidad
count =: #           NB. `count` se asigna al operador de tamaño (número de elementos)
iota =: i.           NB. `iota` se asigna al operador generador de rango
square =: *:         NB. `square` se asigna al operador cuadrático (multiplicación por sí mismo)
add =: +:            NB. `add` se asigna al operador de adición acumulada

NB. Usando las funciones definidas como variables

identity 42          NB. Esperado: 42

count 7              NB. Esperado: 1 (porque # de un número devuelve 1)
count 1 2 3 4        NB. Esperado: 4 (cuenta los elementos en el array)

iota 5               NB. Esperado: 0 1 2 3 4 (generar un rango hasta 5)
square 3             NB. Esperado: 9 (3^2)

add 3 5 6
