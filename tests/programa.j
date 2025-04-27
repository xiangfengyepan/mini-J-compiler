function fibo(n)
    if. n = 0 do.
        return 0
    end.
    if. n = 1 do.
        return 1
    end.
    return fibo(n-1) + fibo(n-2)
end.

main
    a =: 1
    while. a <> 7 do.
        fibo(a)
        a =: a + 1
    end.
end.