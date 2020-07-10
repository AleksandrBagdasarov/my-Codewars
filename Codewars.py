# energy = '150 132 110 186 103 229 179 224 230 113 224 202'
# norm = 148
# norm_cost = 3.67
# over_norm_cost = 4.83

energy = str(input())
norm = int(input)
norm_cost = float(input())
over_norm_cost = float(input())

count_energy = []
count_cost = 0

energy = energy.split()
for x in energy:
    x = int(x)
    count_energy.append(x)
    if x < norm:
        count_cost += x * norm_cost
    else:
        over = x - norm
        count_cost += over * over_norm_cost
        count_cost += norm * norm_cost

print("Сумма: %6d кВт ч, стоимость %7.2f руб" % (sum(count_energy), count_cost))