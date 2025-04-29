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
    result =: sumArray(myArray)
    maxValue =: maxArray(myArray)
    minValue =: minArray(myArray)
    meanValue =: meanArray(myArray)
    reversed =: reverseArray(myArray)
    evens =: filterEven(myArray)
    squares =: mapSquare(myArray)
    contains5 =: arrayContains(myArray; 5)
    contains9 =: arrayContains(myArray; 9)

    n =: 20
    i =: 0
    primes =: i.0
    while. i <= n do.
        if. isPrime(i) do.
            primes =: primes , i
        end.
        i =: i + 1
    end.


    write "Sum of array:"
    result
    write "Max value:"
    maxValue
    write "Min value:"
    minValue
    write "Mean value:"
    meanValue
    write "Reversed array:"
    reversed
    write "Even numbers:"
    evens
    write "Squares of elements:"
    squares
    write "Primes up to 20:"
    primes
    write "Array contains 5:"
    contains5
    write "Array contains 9:"
    contains9
end.
