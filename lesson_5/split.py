def split(my_str, separator=None, limit=None):
    my_list = []
    temp_str = ''
    my_str = my_str.lstrip(' ')
    if separator is None:
        if ' ' in my_str:
            separator = " "
    elif separator not in my_str:
        return [my_str]
    elif separator == '':
        raise ValueError('empty separator')
    if limit is None or limit > my_str.count(separator):
        limit = my_str.count(separator)
    while limit > 0:
        for i in range(limit):
            for j in my_str[: my_str.find(separator)]:
                temp_str += j
            my_list.append(temp_str)
            temp_str = ''
            my_str = my_str[my_str.find(separator) + len(separator):]
            limit -= 1
    else:
        my_list.append(my_str)
    return my_list

print(split('       1 2  3 44 555   6666   77777   ',None,5))
print('       1 2  3 44 555   6666   77777   '.split(None,5))
