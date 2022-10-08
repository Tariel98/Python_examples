def cesar(my_str):
	simbol = int(input("Enter simbol count: "))
	codet_str = ""
	for i in my_str:
		i = ord(i) - simbol
		codet_str += chr(i)
	return codet_str

my_str = input('Please enter text: ')
print(f'Coded text will be: \"{cesar(my_str)}\"')
		 

