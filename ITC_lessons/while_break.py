#!/bin/python3 



weather = int(input('Type whater: '))
meters = 0

while weather > 15:
	meters  += 20
	weather -= 2
	if weather <= 15:
		break
	meters  += 10
print('Ancav ', meters, 'Meters')
