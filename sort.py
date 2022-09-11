#!/bin/python3


num_1 = int(input('First number: '))
num_2 = int(input('Second number: '))
num_3 = int(input('Third number: '))

if num_1 > num_2:
	maximum = num_1
else:
	maximum = num_2

if num_3 > maximum:
	maximum = num_3

print('Mamximum number is:', maximum)
