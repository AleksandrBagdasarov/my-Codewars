def root(n):
    new_n = 0
    for x in str(n):
        new_n += int(x)
    if len(str(new_n)) > 1:
        return digital_root(new_n)
    else:
        return new_n

def digital_root(n):
    if len(str(n)) > 1:
        return root(n)
    else:
        return n

    
        




digital_root(16)# 7)
digital_root(942)# 6)
digital_root(132189)# 6)
digital_root(493193)# 2)