#!/bin/python3 


number = int(input('Type number: '))

#number // 10
#number %  10

summ = 0
while number !=0:
	last_num = number % 10
	print(last_num)
	if last_num == 5:
		print('Obnarujen razriv:')
		break 
	summ += last_num
	number //= 10
print('Sum:', summ)



