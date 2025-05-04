NB. Asignación de operadores a variables
identity =: ]        NB. `identity` se asigna al operador de identidad
count =: #           NB. `count` se asigna al operador de tamaño (número de elementos)
iota =: i.           NB. `iota` se asigna al operador generador de rango
plus =: +            NB. `plus` se asigna al operador de suma
power =: ^:          NB. `power` se asigna al operador de potencia (exponente)
square =: *:         NB. `square` se asigna al operador cuadrático (multiplicación por sí mismo)
add =: +:            NB. `add` se asigna al operador de adición acumulada
subtract =: -:       NB. `subtract` se asigna al operador de resta acumulada
divide =: %          NB. `divide` se asigna al operador de división

NB. Usando las funciones definidas como variables

NB. Identidad
identity 42          NB. Esperado: 42

NB. Tamaño (conteo de elementos)
count 7              NB. Esperado: 1 (porque # de un número devuelve 1)
count 1 2 3 4        NB. Esperado: 4 (cuenta los elementos en el array)

NB. Generador de rango (iota)
iota 5               NB. Esperado: 0 1 2 3 4 (generar un rango hasta 5)

NB. Valor absoluto (identidad en este caso)
plus 7               NB. Esperado: 7
plus _3              NB. Esperado: _3 (en J, `+` no aplica abs por defecto)

NB. Operadores cuadráticos (adverbios unarios)
square 3             NB. Esperado: 9 (3^2)
NB. power 3              NB. Esperado: 27 (3^3)

NB. NB. Reducción con adición acumulada
NB. fadd 1 2 3 4        NB. Esperado: 10 (1 + 2 + 3 + 4)

NB. NB. Reducción con multiplicación acumulada
NB. square / 1 2 3 4     NB. Esperado: 576 (1*1 * 2*2 * 3*3 * 4*4)
NB. plus / 1 2 3 4       NB. Esperado: 10 (1 + 2 + 3 + 4)

NB. NB. Reducción con resta acumulada
NB. subtract / 10 5 2    NB. Esperado: 3 (10 - 5 - 2)

NB. NB. Reducción con división acumulada
NB. divide / 100 2 5     NB. Esperado: 10 (100 ÷ 2 ÷ 5)
