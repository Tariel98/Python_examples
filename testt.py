#!/bin/python3

#
#a = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
#print(type(a))
#

tiket_number = int(input('Type your ticket number: '))
summ_first = (tiket_number // 100000) + (tiket_number // 10000 % 10) + (tiket_number // 1000 % 10) 
summ_end   = (tiket_number // 100 % 10) + (tiket_number // 10 % 10) + (tiket_number % 10) 
while summ_first != summ_end:
	tiket_number = int(input('Type your ticket number: '))    
	summ_first = (tiket_number // 100000) + (tiket_number // 10000 % 10) + (tiket_number // 1000 % 10) 
	summ_end   = (tiket_number // 100 % 10) + (tiket_number // 10 % 10) + (tiket_number % 10) 	
print('You win!')
