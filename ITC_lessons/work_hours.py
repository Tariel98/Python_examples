#!/bin/python3


hours  = int(input('Enter hours worked: '))
credit = int(input('Enter your loan balance: ')) 
food   = int(input('Enter food expenses: '))

salary = (200 * hours) / (2 ** 3) + hours
credit_food_sum = credit + food

if salary >= credit_food_sum:
	print('Enough hours. You can rest!')
else:
	print('There are not enough hours. Have to work!')
