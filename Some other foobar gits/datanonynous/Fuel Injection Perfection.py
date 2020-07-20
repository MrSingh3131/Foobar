def answer(n):
    n = int(n)
    count = 0
    while n > 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        elif n == 3 or n%4 == 1:
            n = n - 1
        else:
            n = n + 1
        count = count + 1
    return count

print(answer(9999))

