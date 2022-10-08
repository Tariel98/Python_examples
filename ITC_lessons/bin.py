while True:
	number = input('Please enter number: ')
	try:
		number = int(number)
	except ValueError:
		print('entered wrong value')
	else:

		str_bin = ''

		while number > 1:
			y = number % 2
			number //= 2
			str_bin += str(y)
		str_bin += '1'
		print(f'The binary number will be: {str_bin[::-1]}')
		break
