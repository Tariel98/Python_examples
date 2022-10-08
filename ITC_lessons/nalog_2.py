#!/bin/ptyhon3


money = int(input('Type money: '))

if money <= 10000:
	nal = money * 13 / 100
	print('Yor tax constitutes։', nal)
elif money > 10000 and money <= 50000:
	difference  = money - 10000
	nal = (difference * 20 / 100) + (10000 * 13 / 100) 
	print('Yor tax constitutes։', nal)
elif money > 50000:
	difference = money - 50000
	if difference > 10000:
		difference2 = difference - 10000
		nal = (difference * 30 / 100) + (difference2 * 20 / 100) + (10000 * 13 / 100)
	nal = (difference * 30 / 100) + (10000 * 13 / 100)
	print('Yor tax constitutes։', nal)
	
