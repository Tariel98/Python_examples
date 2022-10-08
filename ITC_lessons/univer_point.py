#!/bin/python3



examination_1 = int(input('Enter the number of points in the Russian language: '))
examination_2 = int(input('Enter your math score: '))
examination_3 = int(input('Enter the number of points in computer science: '))

sum_examination_points =  (examination_1 + examination_2 + examination_3)

if sum_examination_points >= 270:
	print('Congratulations, you have entered the budget!')
else:
	print("Unfortunately, you didn't make it to the budget.") 
