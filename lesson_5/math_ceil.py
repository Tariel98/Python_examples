from math import ceil

def round_up(num1,num2):
	print(f'The rounded value will be obtained: {ceil(num1 / num2)}')


num1 = input('Pleas enter first number: ')
num2 = input('Pleas enter second number: ')

try:
	num1 = float(num1) or int(num1)
	num2 = float(num2) or int(num2)
except ValueError:
	print('Pleas enter number')
else:	
	round_up(num1,num2)
