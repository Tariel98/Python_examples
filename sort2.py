#!/bin/python3


num_1 =  int(input('Type first  number: '))
num_2 =  int(input('Type second number: '))
num_3 =  int(input('Type third  number: '))


if num_1 > num_2 and num_1 > num_3: 
	print(num_1)
elif num_2 > num_1 and num_2 > num_3:
	print(num_2)
else:
	print(num_3)
