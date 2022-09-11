#!/bin/python3


milege = int(input('Enter mileage: '))
todays_date = int(input("Enter today's date: "))

first_num  = milege // 100
second_num = milege // 10 % 10
third_num  = milege % 10

sum_numbers = first_num + second_num + third_num

if sum_numbers >= todays_date:
	print('Reset')
	print('Milege: 0')
else:
	print("Didn't break today.")
	print('Milege:', milege)
