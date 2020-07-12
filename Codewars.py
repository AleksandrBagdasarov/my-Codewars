import numpy as np

import numpy.linalg as alg


a = np.array([[1, -3, -2, 1],[2, 4, 3, -1],[5, -2, 0, -2], [1, 4, 1, -1]])

print("A :\n", a)
# Вычислить определитель квадратного блока  матрицы, состоящего из элементов на пересечении первых двух строк  и столбцов с номером 1 и 2, вывести результат:

det_bl = alg.det(a[:2,1:3])

print("det(block) = ", det_bl)
# Вычислить сумму элементов главной диагонали.матрицы A, вывести результат:

sum_diag = np.sum(np.diag(a))

print("sum_diag =  ", sum_diag)
# Найти максимальные элементы каждого столбца:

max_col = np.max(a, 0)

print("max_col :", max_col)
# Найти минимальные элементы каждой строки:

min_row = np.min(a, 1)

print("min_row :", min_row)