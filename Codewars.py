def persistence(n):
    counter = 0
    return qqq(n,counter)

def qqq(n,counter):
    str_n = str(n)
    str_new_n = str_n[0]
    int_new_n = int(str_new_n)
    if n > 9:
        counter += 1
        for x in str_n[1:]:
            int_new_n *= int(x)
        return qqq(int_new_n, counter)
    else:
        return counter
            
        


persistence(39)# 3)
persistence(4)# 0)
persistence(25)# 2)
persistence(999)# 4)