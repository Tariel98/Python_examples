def tuple_list_sum(numbers1,numbers2):
	cutting = [x for x in list(numbers1) + list(numbers2) if x not in numbers1 or x not in numbers2]
	print(f'The difference between {numbers1} & {numbers2} will be։ {cutting}')
	print(f'The sum of the elements of the differences will be։ {sum(cutting)}')



	
