from string import ascii_lowercase, punctuation

def pangram_cheker(my_str):
	my_str = set(my_str.lower())
	my_str -= set(punctuation + ' ')
	if my_str == set(ascii_lowercase):	
		print('Pangram')
	else:
		print('Pangram che')


my_str = 'Sphinx of black, quartz; judge my vow.'

pangram_cheker(my_str)
