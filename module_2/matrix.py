def get_matrix(n, m, value):
    matrix = [] + []
    for row in range(n):  # внешний цикл для строк
        matrix.append([])
        for column in range(m):  # внутренний цикл для столбцов
            matrix[row].append(value)


    print(matrix)


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 6, 42)
result3 = get_matrix(5, 2, 15)

print(result1)
print(result2)
print(result3)
