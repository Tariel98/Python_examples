#!/bin/python3


hour = int(input('Please type hour: '))

if 8 > hour > 22 or 14 <= hour <= 15 or 10 <= hour < 12 or 18 <= hour <= 20: 
	print('Посылку получить нельзя')
else:
	print('Можно получить посылку')	
