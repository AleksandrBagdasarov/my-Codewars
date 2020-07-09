#from math import atan, pi
#
#
#
#
#def arcctan(x):
#    return (pi/2) - atan(x)
#
#
#t = int(input())
#c = 172
#T1 =  2000
#naselenie = (c/45) * arcctan((T1-t)/45)
#print(naselenie)
#years_str_list = ['123','200']
#years_list = [int(x) for x in years_str_list]
#print(years_list)
#x = 2020
#y = naselenie
#print("%5d - %6.3f миллиард(ов)" % (x, y))


from math import atan, pi



def arcctan(x):
    return (pi/2) - atan(x)

def compute_population(t):
   #вычислить численность населения для года t по формуле
    c = 172
    T1 =  2000
    return (c/45) * arcctan((T1-t)/45)


#ввести строку с перечисленными через пробел годами
line = input()

# преобразовать строку в список из строковых значений годов
years_str_list = line.split()

# вычислить количество элементов в списке
n = len(years_str_list)

# сформировать список years_list на основе years_str_list, 
years_list = [int(x) for x in years_str_list]


# создать список population_list, каждый элемент которого вычисляется
population_list = []
for x in years_list:
    population_list.append(compute_population(x))


# в цикле для каждого года вывести численность населения, для вывода использовать
for x, y in zip(years_list, population_list):
    print("%5d - %6.3f миллиард(ов)" % (x, y))
# формат "%5d - %6.3f миллиард(ов)"