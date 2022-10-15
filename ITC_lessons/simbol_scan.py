from string import punctuation

my_str = input('Pleas enter text: ')
for i in my_str:
    if i in punctuation:
        print(f'this element is a symbol \'{i}\' ')
        break
