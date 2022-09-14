number_x = input('Please enter number: ')
if (number_x[0] == '-' and number_x[1:].isdigit()) or number_x.isdigit():
    number_x = int(number_x)
elif number_x[0] == '0' and number_x[1:2] == '.' and number_x[2:].isdigit():
	number_x = float(number_x)
else:
    print('The entered character is not number!')
    exit()

number_y = input('Please enter exponent: ')
if number_y[0] == '-' and number_y[1:].isdigit() or number_y.isdigit():
	number_y = int(number_y)
else:
	print('The entered character is not number!')
	exit()

result = 1

if number_y < 0:
    number_y *= -1
    for i in range(number_y):
        result *= number_x
    print(1/result)
else:
    for i in range(number_y):
        result *= number_x
    print(result)

