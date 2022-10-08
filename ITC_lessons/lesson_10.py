#!/bin/python3


profit = int(input('Type money: '))
if profit < 10000:
	tax = profit * 13 / 100
	print('Nalog 13% = ', tax)
elif profit < 50000:
	tax = profit * 20 / 100
	print('Nalog 13% = ', tax)
else:
	tax = profit * 30 / 100
	print('Nalog 30% = ', tax)
