#
#tiket_number = int(input('Type your ticket number: '))
#summ_first = (tiket_number // 100000) + (tiket_number // 10000 % 10) + (tiket_number // 1000 % 10)
#summ_end   = (tiket_number // 100 % 10) + (tiket_number // 10 % 10) + (tiket_number % 10)
#while summ_first != summ_end:
#    tiket_number = int(input('Type your ticket number: '))
#    summ_first = (tiket_number // 100000) + (tiket_number // 10000 % 10) + (tiket_number // 1000 % 10)
#    summ_end   = (tiket_number // 100 % 10) + (tiket_number // 10 % 10) + (tiket_number % 10)
#print('You win!')
#
#********************************************************************************************************************************************
#********************************************************************************************************************************************
#quantity_pos = 0
#quantity_neg = 0
#
#while True:
#	number = int(input('Type number: '))	
#	if number == 0:
#		break
#	elif number > 0:
#		quantity_pos += 1
#	else:
#		quantity_neg += 1
#print(f'Quantity of positive answers: {quantity_pos}')
#print(f'Quantiti of negative answers: {quantity_neg}')	
#********************************************************************************************************************************************

print('Начался 8-часовой рабочий день')
print('')
time = 1
zadacha1 = 0
jenazv = 0

while time <= 8:
	print(f'{time}-й час')
	print('')
	time += 1
	zadacha = int(input('Сколько задач решит Максим? '))
	print('')
	zadacha1 += zadacha
	jena = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
	jenazv += jena	
print(f'Рабочий день закончился. Всего выполнено задач: {zadacha1}')	
if jenazv > 0:
	print('Нужно зайти в магазин.')
	
