import math

def answer(area):
    submit = []

    if area == 0 or area <0:
        submit.append(0)

    #area = abs(area)
    counter = area

    while area > 0:
        if math.sqrt(area).is_integer():
            submit.append(area)
            area = counter - area

            if area == 3:
                submit.append(1)
                submit.append(1)
                submit.append(1)
                break

            if area == 1:
                submit.append(1)
                break

        area = area - 1

    return submit



print(answer(-6))

# for x in range(1,13,1):
#     print(answer(x))