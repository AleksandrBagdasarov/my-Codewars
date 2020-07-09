

def compute_payment(s, n, k):
    # вычисление ежемесячного платежа
    bank = []
    for t in range(1, n + 1):
        x = (s / n) + (s - (t - 1) * (s / n)) * (k / (12 * 100))
        bank.append(x)
        print("%2d месяц - %8.2f руб" % (t, x))
    print("Доход банка - %6.2f руб" % (sum(bank) - s))
# s=int(input())
# n=int(input())
# k=int(input())
s = 300000
n = 6
k = 20

compute_payment(s, n, k)