#!/bin/python3

num = int(input('Type number: '))

first_num  = num % 10000  // 1000 
second_num = num % 1000   // 100
third_num  = num % 100    // 10
for_num    = num % 10

print(f'{for_num}{third_num}{second_num}{first_num}')
