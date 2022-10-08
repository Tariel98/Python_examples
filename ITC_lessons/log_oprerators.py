#!/bin/python3


year = int(input('Typr yesr: '))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
	print('Visokosniy')
else:	
	print('Vesiokosniy')
