#!/bin/python3


bank = int(input('How much money in card: '))


if bank >= 75000:
	bank -= 75000
	print('Kursy hajoxutyamb gnvel e')
	if bank < 5000:
		bank += 1000
		print('Sdelana skidka')
else:
	print('You are not a have money!')
print('Lav or dzez!')
print('Ostatok na schetu', bank)
