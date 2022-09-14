while True:
	number = input('Please enter number: ')
	x = 0
	if number.isdigit():
		for i in number:
			x += 1
		print(x)
	else:
		print('Please enter correct number')
