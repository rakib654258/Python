import re
num = ''
def collatz(number):
        if number % 2 == 0:
            num = (number//2)
            print(num)
            if num == 1:
                exit()
        elif number % 2 == 1:
            num = (3*number+1)
            print(num)
try:
    while num != 1:
        collatz(int(input()))
except ValueError as e:
         print('ValueError: ', e)

