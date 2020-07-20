def answer(l):
    factor = [[]] * len(l)
    for i in range(1, len(l)):
        factor[i] = [j for j in range(i) if l[i] % l[j] == 0]
    count = 0
    for i in range(2, len(l)):
        count += sum(len(factor[j]) for j in factor[i])
    return count


print(answer([1, 1, 1]))
print(answer([1, 2, 3, 4, 5, 6]))
