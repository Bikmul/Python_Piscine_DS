import timeit
import sys
from functools import reduce

def main():
    j = (int)(sys.argv[3])
    i = (int)(sys.argv[2])
    if (sys.argv[1]) == "loop":
        print(f'{timeit.timeit(lambda: loop_method(j), number = i)}')
    elif (sys.argv[1]) == "reduce":
        print(f'{timeit.timeit(lambda: reduce_method(j), number = i)}')

def loop_method(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i**2
    return(sum)

def reduce_method(number):
    return reduce((lambda res, i: res + i ** 2), range(number + 1))

if __name__ == '__main__':
    if len(sys.argv) == 4:
        main()


















if __name__ == '__main__':
    if len(sys.argv) == 3:
        main()