#!/bin/pyhton3


product  = int(input('Type price chek: '))
delivery = int(input('Type price delivery: '))
discount = 0

if product > 10000:
	print('Good chek! Deloveri snijena dvoe')
	delivery /= 2
	if product % 2 == 0:
		print('You are have gift:')
		discount = 500
price = product + delivery - discount
print('Polnaya stoimosttovarov:', price)
