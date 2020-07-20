data = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 6, 7]

def answer(data, n):

    # Dictionary Comprehension
    new = {x:data.count(x) for x in data}

    #Get keys and values from new dict array
    keys, values = new.keys(), new.values()

    print(keys)
    print(values)

    keys = list(keys)
    values = list(values)

    print(keys)
    print(values)

    # List Comprehension
    submit = [
        keys[k-1]
        for k in keys
        if values[k-1] <= n
        ]

    for k in keys: # Demonstration that the iterable starts at 1, not 0
        print(k)

    return submit

print(answer(data, 1))



