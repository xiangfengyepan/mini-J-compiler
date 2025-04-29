function isPrime(n)
    if. n < 2 do.
        return 0
    end.
    i =: 2
    while. i * i <= n do.
        if. i | n = 0 do.
            return 0
        end.
        i =: i + 1
    end.
    return 1
end.

main 
    write f"2 es primer? {isPrime(2)}"

end.