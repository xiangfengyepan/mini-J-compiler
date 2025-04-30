function sumArray(arr)
    i =: 0
    total =: 0
    while. i < #arr do.
        total =: total + (i { arr)
        i =: i + 1
    end.
    return total
end.

function meanArray(arr)
    return sumArray(arr) % #arr
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

function minArray(arr)
    i =: 1
    minVal =: 0 { arr
    while. i < #arr do.
        if. (i { arr) < minVal do.
            minVal =: i { arr
        end.
        i =: i + 1
    end.
    return minVal
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

function filterEven(arr)
    i =: 0
    newArr =: i.0
    while. i < #arr do.
        if. 2 | (i { arr) = 0 do.
            newArr =: newArr , (i { arr)
        end.
        i =: i + 1
    end.
    return newArr
end.

function mapSquare(arr)
    i =: 0
    result =: i.0
    while. i < #arr do.
        result =: result , ((i { arr) * (i { arr))
        i =: i + 1
    end.
    return result
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

function arrayContains(arr; val)
    i =: 0
    while. i < #arr do.
        if. (i { arr) = val do.
            return 1
        end.
        i =: i + 1
    end.
    return 0
end.

main
    myArray =: 3 9 1 7 2
    n =: 20
    i =: 0
    primes =: i.0
    while. i <= n do.
        if. isPrime(i) do.
            primes =: primes , i
        end.
        i =: i + 1
    end.

    write f"Sum of array: {sumArray(myArray)}"
    write f"Max value: {maxArray(myArray)}"
    write f"Min value: {minArray(myArray)}"
    write f"Mean value: {meanArray(myArray)}"
    write f"Reversed array: {reverseArray(myArray)}"
    write f"Even numbers: {filterEven(myArray)}"
    write f"Squares of elements: {mapSquare(myArray)}"
    write f"Primes up to 20: {primes}"
    write f"Array contains 5: {arrayContains(myArray; 5)}"
    write f"Array contains 9: {arrayContains(myArray; 9)}"
end.

