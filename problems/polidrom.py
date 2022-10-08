
def polidrom(text):
	text = text.lower()	
	if text.replace(' ', '') == text[::-1].replace(' ', ''):
		print('This is text is polidrome.')
	else:
		print('This text is not polidrome.')	

text = input('Enter tex: ')

polidrom(text)
