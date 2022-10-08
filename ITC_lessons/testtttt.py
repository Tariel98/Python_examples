#!/bin/python3


print('Задача 9. Прогрессивный налог 2')
income = int(input('enter your income: '))
if income < 10000:
    print('you should pay', income * 13 / 100)
elif income < 50000:
    print('you should pay', (income - 10000) * 20 / 100 + 1300)
else:
    print('you should pay', (income - 50000) * 30 / 100 + 9300)
