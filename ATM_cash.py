#!/bin/python3


withdraw_sum = int(input('Enter the amount you want to withdraw: '))
divide = withdraw_sum % 100

if divide == 0:
	print('Please wait. Your money will be cashed soon!')
else:
	print('This amount cannot be withdrawn. Go to another ATM.')
