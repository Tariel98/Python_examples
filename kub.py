#!/bin/python3

num_1 = int(input('Type first number: '))
num_2 = int(input('Type second number: '))
num_3 = int(input('Type third number: '))

if num_1 == num_2 and num_1 == num_3 and num_2 == num_3:
	print('3')
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
	print('2')
else:
	print('0')

