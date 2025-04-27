function sm(x; y)
    return x + y
end.

main
    a =: 1 + 2 
    b =: a * 2

    x =: 0          NB. Inicializamos x en 0
    y =: 5          NB. Inicializamos y en 5
    
    sm(a; b)

    while. x < y do.
        NB. Dentro del bucle, incrementamos x
        x =: x + 1
    end.
    x

end.