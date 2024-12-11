my_dict = {'cat': 2, 'dog': 3}
print(my_dict)

print(my_dict['cat'])
my_dict['dog']= 5
print(my_dict)

my_dict['bird'] = 1
my_dict['spider'] = 7
print(my_dict)

del my_dict['dog']
print(my_dict)

print(my_dict.get('cat'))
print(my_dict)

my_set = {1, 1, 3, 3, 'change', True, 'change'}
print(my_set)

print(my_set.add(4))
print(my_set.add('github'))

print(my_set.discard('change'))
print(my_set)


