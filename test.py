#!/bin/pyhton3

#
#product  = int(input('Type price chek: '))
#delivery = int(input('Type price delivery: '))
#discount = 0
#
#if product > 10000:
#	print('Good chek! Deloveri snijena dvoe')
#	delivery /= 2
#	if product % 2 == 0:
#		print('You are have gift:')
#		discount = 500
#price = product + delivery - discount
# print('Polnaya stoimosttovarov:', price)
#
#
#animals_1 = {"dog", "cat", "pig", "horse", "lamb"}
#animals_2 = {"pig", "sheep", "rabbit", "dog"}
#
#animals_3 = animals_1 ^ animals_2
#print(animals_3)
#

animals_1 = {"dog", "cat", "pig", "horse", "lamb"}
animals_2 = {"pig", "sheep", "rabbit", "dog"}
animals_3 = set()

for x in animals_1:
	for y in animals_2:
		if x != y:
			animals_3 += set(x)
			animals_3 += set(y)
		else:
			continue
print(animals_3)
