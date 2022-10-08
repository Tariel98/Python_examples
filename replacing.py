#!/bin/python3 

#my_list = [1, 2, 3,3] 
#my_set = set(my_list)
#print(f'{len(my_list - my_set)}')
#print('*******************************************')
#my_dict = {"Tariel": "Hasmik", "Phone": "Iphone", "Car": "Mercedes"}
#print(my_dict.items())
#print('**************************')
#brands = ["Iphone", "Samsung", "Xiaomi"]
#phone = brands
#print(phone)
#print(brands)


my_dict = {2: 8, 5: 20, 3: 15, 6: 2, 11:20}

print(my_dict.keys())

print(sum(my_dict.keys()))
print('****************************************')

my_str = "Silicon:Valley:is:a:region:in:Northern:California:that:serves:as:a:global:center:for:high:technology:and:innovation"
new_str = my_str.replace(':',' ')
print(new_str)

print('****************************************')

item = "Computer Name"
item = item + ' '  +  item[::-1]
print(item.lower())

print('****************************************')
my_dict = {'Tariel':'milioner', 'Hasmik':'milionerka'  } 
x = ('key1', 'key2', 'key3')
y = (10,20,30,)

dic =  my_dict.fromkeys(x,y)
print(dic)
