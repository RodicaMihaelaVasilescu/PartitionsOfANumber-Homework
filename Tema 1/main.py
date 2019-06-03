#main.py
from modules import *

n = int(input('Enter the number n: '))

print('1. Partitions of the number %d' %n)
print('2. The %d-th palindrome' %n)
print('3. Display subsets with the sum equal to %d' %n)
print('4. Display the number %d' %n)
print('5. Exit\n')

option = int(input('Enter the option: '))
while option != 0:
    if option == 1:
        s = 0
        x = [0 for x in range(1000)]
        partitie(1, 0, x, n)
    if option == 2:
        print(palindrom(n))
    if option == 3:
        x = [0 for x in range(1000)]
        x[0] = 1
        submultime(1, n, x, n)
    if option == 4:
        print(n)
    if option == 5:
        exit()
    option = int(input('Enter the option: '))