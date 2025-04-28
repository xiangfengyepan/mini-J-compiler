function sumArray(arr)
    i =: 0
    total =: 0
    while. i < #arr do.
        total =: total + (i { arr)
        i =: i + 1
    end.
    return total
end.

function maxArray(arr)
    i =: 1
    maxVal =: 0 { arr
    while. i < #arr do.
        if. (i { arr) > maxVal do.
            maxVal =: i { arr
        end.
        i =: i + 1
    end.
    return maxVal
end.

function reverseArray(arr)
    i =: (#arr) - 1
    newArr =: i.0
    while. i >= 0 do.
        newArr =: newArr , (i { arr)
        i =: i - 1
    end.
    return newArr
end.

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
    myArray =: 3 9 1 7 2
    result =: sumArray(myArray)
    maxValue =: maxArray(myArray)
    reversed =: reverseArray(myArray)
    n =: 20
    i =: 0
    primes =: i.0
    while. i <= n do.
        if. isPrime(i) do.
            primes =: primes , i
        end.
        i =: i + 1
    end.

    result
    maxValue
    reversed
    primes
end.