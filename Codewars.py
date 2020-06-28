def find(i, seq):
    s = seq.count(seq[i])
    if s % 2 == 0:
        i += 1
        return find(i, seq)
    else:
        return seq[i]



def find_it(seq):
    i = 0
    return find(i, seq)



find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])# 5)
find_it([1,1,2,-2,5,2,4,4,-1,-2,5])# -1); 
find_it([20,1,1,2,2,3,3,5,5,4,20,4,5])# 5);
find_it([10])# 10);
find_it([1,1,1,1,1,1,10,1,1,1,1])# 10);
find_it([5,4,3,2,1,5,4,3,2,10,10])# 1);