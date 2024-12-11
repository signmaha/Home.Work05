immutable_var = (1, 2, 'a','b', True)
print( "tuple_:", immutable_var)

#immutable_var =это кортеж, попытка изменить его выдаст ошибку, т.к кортеж неподдерживает замену элементов
#например immutable_var[3] = 'g'

mutable_list = [2, 5, 'j', 'k', False]
mutable_list[0] = 'h'
mutable_list[-1] = True

print(mutable_list)

