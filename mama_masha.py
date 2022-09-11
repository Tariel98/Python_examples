#!/bin/python

amout_money = int(input('Type amout of money: '))
cheese = 60
ice_cream = 20

if amout_money >= cheese:
	amout_money -= 60
	print('Enough money for cheese!')
	if amout_money >= 20:
		amout_money -= 20
		print('And ice cream too!')
	else: 
		print('Not enough money')
	print('Amout of money',amout_money)
else: 
	print('Not enough money!')


