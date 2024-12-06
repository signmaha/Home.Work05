def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(6, 'строчки')
print_params(5, 'lol', True)
print_params(13)

print('print_params(b = 25)')
print('print_params(c = [1, 2, 3]')

values_list = [2, 'well', None]

values_dict = {'a': 3, 'b': 'string', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = (32, 'number')

print_params(*values_list_2, 4)
print(*values_list_2, 4)
