#!/bin/python3


number_Kostia = int(input('Number Kotia: '))
number_owner  = int(input('Nuber Owners: ')) 

if number_Kostia >= number_owner:
	print('The difference:',number_Kostia - number_owner)
	print('Kostia will pay!')
else:
	print('The amount is: ', number_Kostia + number_owner)
	print('Owner pays!')
	print('Game Over!')
	
