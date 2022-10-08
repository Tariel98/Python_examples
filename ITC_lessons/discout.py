#!/bin/python3


money = int(input('How much money is in the account? '))

if money >= 75000:
	money -= 75000
	print('Course successfully purchased!')
	if money < 5000:
		money += 1000
		print('Made a discount!')
	print('Account balance:',money )
else:
	print('You are not a have much money!')
	print('Account balance:',money )
print('Have nice day!')
