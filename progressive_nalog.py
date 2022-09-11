#!/bin/python3


money =  int(input('Type money: '))

if money <= 10000:
	nal = money * 13 / 100
	print('Nalog 13% = ', nal)
elif money <= 50000:
	nal = money * 20 / 100
	print('Nalog 20% = ', nal)
else:
	nal = money * 30 / 100
	print('Nalog 30% ', nal)
	
