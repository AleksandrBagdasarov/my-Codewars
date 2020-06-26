def high_and_low(numbers):
    a = []
    for x in numbers.split():
        a.append(int(x))
    return f'{str(max(a))} {str(min(a))}'

high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")# "542 -214")