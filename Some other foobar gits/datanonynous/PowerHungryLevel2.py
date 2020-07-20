def answer(xs):
    submit = []
    positiveProduct = 1
    negativeEvenProd = 1
    negativeOddProd = 1

    for x in xs:
        #culled out non zero values
        if x != 0:
            submit.append(x)
    submit = sorted(submit)
    print("Complete sorted list: %s" %submit)

    negNum,posNum = [i for i in submit if i<0],[j for j in submit if j>0]
    print("Negative numbers: %s" %negNum)
    print("Positive numbers: %s" %posNum)

    for item in posNum:
        positiveProduct = positiveProduct * item

    lengthOfNegative = len(negNum)
    lengthOfPositive = len(posNum)

    #is even
    if lengthOfNegative % 2 == 0:
        for itemEven in negNum:
            negativeEvenProd = negativeEvenProd * itemEven
    #is odd, subtract last element then multiply together
    if lengthOfNegative == 1 and lengthOfPositive == 0:
        negativeOddProd = int(negNum[0])
    elif lengthOfNegative % 2 > 0:
        del negNum[-1]
        for itemOdd in negNum:
            negativeOddProd = negativeOddProd * itemOdd

    finalProduct = positiveProduct * negativeEvenProd * negativeOddProd

    if xs[0] == 0:
        finalProduct = 0;

    finalProduct = str(finalProduct)

    return finalProduct

print(answer([-5]))
print(answer([2,0,2,2,0]))
print(answer([-2,-3,4,-5]))
print(answer([9]))
print(answer([0]))
