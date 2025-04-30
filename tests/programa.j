myArray =: 3 9 1 7 2

i =: 0
newArr =: i.0
while. i < #myArray do.
    if. 2 | (i { myArray) = 0 do.
        newArr =: newArr , (i { myArray)
    end.
    i =: i + 1
end.

newArr