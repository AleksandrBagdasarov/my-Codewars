import numpy as np

# x = '-1.7 -1.5 -1.3 -0.5 -0.2 0.5 0.6 0.7 1.0 3.0 3.1 3.1 4.3'
# y = '8.7 8.4 8.0 6.5 5.9 4.6 4.4 4.2 3.6 -0.2 -0.4 -0.4 -2.7'

x = str(input())
y = str(input())

x_array = np.array(x.split(), dtype=float)
y_array = np.array(y.split(), dtype=float)


def get_trend_1(x, a):
    y = a[0] * x + a[1]
    return y


def get_trend_2(x, a):
    y = a[0] * (x ** 2) + a[1] * x + a[2]
    return y


def otn_pogr(y, yr):
    pogr = abs((yr - y) / y) * 100
    return pogr


a1 = np.polyfit(x_array, y_array, 1)
a2 = np.polyfit(x_array, y_array, 2)

x_trend1 = [get_trend_1(x, a1) for x in x_array]
x_trend2 = [get_trend_2(x, a2) for x in x_array]

otn_error1 = [otn_pogr(y, x) for y, x in zip(y_array, x_trend1)]
otn_error2 = [otn_pogr(y, x) for y, x in zip(x_trend2, y_array)]


avg_error1 = np.mean(otn_error1)
avg_error2 = np.mean(otn_error2)

if avg_error1 < avg_error2:
    print("%5.3f %5.3f" % (a1[0], a1[1]))
else:
    print("%5.3f %5.3f %5.3f" % (a2[0], a2[1], a2[2]))
