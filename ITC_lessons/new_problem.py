number = int(input('Enter number: '))
isPrime = True
for divider in range(2, number):
	if number % divider == 0:
		isPrime = False
		break
	if isPrime:
		print('Prostoe')
	else:
		print('sostavnoe')
