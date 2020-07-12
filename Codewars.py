from sys import exit
import numpy as np

def restart():
    s = str(input())
    if s.lower() == 'y':
        input_num()
    elif s.lower() == 'n':
        print('Exit Complete!')
        exit(0)

def bin_search(num, array, count):
    if num == array[0]:
        print(f'### {num} Found In {count} Step!')
        print('### Put "Y" to Restart or "N" to Exit')
        restart()
    elif len(array) == 1:
        print(f'### {num} Not in Array')
        print('### Put "Y" to Restart or "N" to Exit')
        restart()
    elif num > array[len(array) // 2] - 1:
        count += 1
        array = array[len(array) // 2 :]
        bin_search(num, array, count)
    elif num < array[len(array) // 2] + 1:
        count += 1
        array = array[: len(array) // 2]
        bin_search(num, array, count)


def input_num():
    try:
        num = int(input('### Put The Number: '))
        count = 1
        array = np.sort(np.random.randint(-20, 20, 40))
        bin_search(num, array, count)
    except ValueError:
        print('### This Is Not A Number!')
        print('### Put "Y" to Restart or "N" to Exit')
        restart()

input_num()
