def compute_differentiated(s, n, k):
    # вычисление ежемесячного платежа
    ka = (k/(12*100))
    bank_differentiated = []
    bank_annuity = []
    for t in range(1, n + 1):
        #  ((((1 + ka) ** n) - 1) / (ka * ((1+ka) ** n)))
        pa = ((ka * ((1+ka) ** n)) / (((1 + ka) ** n) - 1)) * s
        x = (s / n) + (s - (t - 1) * (s / n)) * (k / (12 * 100))
        bank_differentiated.append(x)
        bank_annuity.append(pa)
        print("%2d месяц - (диф.) %8.2f руб - (анн.) %8.2f руб" % (t, x, pa))
    print("Доход банка - (диф.) %6.2f руб - (анн.) %6.2f руб" % (sum(bank_differentiated) - s, sum(bank_annuity) - s,))


# def compute_annuity(s, n, k):
#     ka = (k/(12*100))
#     pa = ((((1 + ka) ** n) - 1) / ka * ((1+ka) ** n)) * s
    
# s=int(input())
# n=int(input())
# k=int(input())
s = 1000000
n = 12
k = 15

compute_differentiated(s, n, k)