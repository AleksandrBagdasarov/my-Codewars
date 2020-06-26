def square_digits(num):
    return int(''.join(list(map(str, [int(x)**2 for x in str(num)]))))




square_digits(9119) # 811181