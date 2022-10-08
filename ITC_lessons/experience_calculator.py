#!bin/python3


points = int(input('Type your points: '))

if points >= 0 and points <= 1000:
	print('Your level is: 1')
elif points > 1000 and points <= 2500:
	print('Your level is: 2')
elif points > 2500 and points <= 5000:
	print('Your level is: 3')
else:
	print('Your level is: 4')
