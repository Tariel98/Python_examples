def split(my_str, separator=None, limit=None):
	my_list = []
	separator = None  # start of 'word'

	for j, c in enumerate(my_str + ' '):
		if c.isspace():
			if separator is not None:
				my_list.append(my_str[separator:j])
				separator =	None
		else:
			if separator is None:
				separator = j
	return my_list


print(split('    Tariel Arakelyan'))
