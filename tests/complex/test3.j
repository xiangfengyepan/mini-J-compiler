NB. Programa J correcto con IF y WHILE

program =: 3 : 0
    x =: 0          NB. Inicializamos x en 0
    y =: 5          NB. Inicializamos y en 5

    while. x < y do.
        NB. Dentro del bucle, incrementamos x
        x =: x + 1
    end.

    NB. Ahora x debería ser igual a y
    result =: 0
    if. x = y do.
        result =: 1  NB. Si x igual a y, ponemos result a 1
    end.

    NB. Devolver resultados como una lista
    x , y , result
)

program ''   NB. Ejecutar el programa
