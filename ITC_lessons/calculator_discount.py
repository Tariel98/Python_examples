#!/bin/python3


product_1 = int(input('Type price first product: '))
product_2 = int(input('Type price second product: '))
product_3 = int(input('Type price third product: '))
sum_product_prices = (product_1 + product_2 + product_3)

if sum_product_prices > 10000:
	print('the total discount will be',sum_product_prices * 10 // 100)
else:
	print('The total amount is:', sum_product_prices) 
