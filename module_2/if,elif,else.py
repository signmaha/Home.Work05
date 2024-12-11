first = int(input('введите первое число:'))
second = int(input('введите второе число:'))
third = int(input('введите третие число:'))

if first == second == third:
    print(3, 'числа равны между собой')

elif first == second or second == third or first == third:
    print(2, 'числа равны между собой')


else:
    print(0, 'равных чисел необноружено')
