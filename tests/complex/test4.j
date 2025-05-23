NB. Asignación de operadores a variables
identity =: ]        NB. `identity` se asigna al operador de identidad
iota =: i.           NB. `iota` se asigna al operador generador de rango
square =: *:         NB. `square` se asigna al operador cuadrático (multiplicación por sí mismo)
add =: +:            NB. `add` se asigna al operador de adición acumulada

NB. Usando las funciones definidas como variables

identity 42          NB. Esperado: 42

iota 5               NB. Esperado: 0 1 2 3 4 (generar un rango hasta 5)
square 3             NB. Esperado: 9 (3^2)

add 3 5 6
