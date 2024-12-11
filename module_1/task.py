averagesscore = {}

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # упорядочитть в алфавитном порядке
print(sorted(students))

employee_grade = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
employee_student = ['Aaron', 'Bilbo', 'Johny', 'Khendrik', 'Steve']

for student, grade in zip(students, grades):
    averagesscore[student] = sum(grade) / len(grade)

print(averagesscore)

# grade_1 = ((5+3+3+5+4)/5)
# grade_2 = ((2+2+2+3)/4)
# grade_3 = ((4+5+5+2)/4)
# grade_4 = ((4+4+3)/3)
# grade_5 = ((5+5+5+4+5)/5)
# print(grades_1, grades_2, grades_3, grades_4, grades_5)

# for student, grade in zip(students, grades):
# print(student, grade)


# grades = [5, 3, 3, 5,4]
# total = sum(grades)
# print(total)

# names = list(students)


# averagesscore.update({'Aaron'[4]:sum(grades[1] /len(grades[1]})
