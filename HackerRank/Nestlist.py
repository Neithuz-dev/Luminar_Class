n  = int(input())

students = []

for i in range(n):
    name = input()
    grade = float(input())
    students.append([name,grade])
# print(students)


grade = []

for student in students:
    grade.append(student[1])
grade.sort()

# print(grade)

lowest = grade[0]

for grades in grade :
    if grades > lowest : #37.2 >37.2 , 37.21>37.2
        second_lowest = grades
        break

name = []

for student in students:
    if student[1] == second_lowest:
        name.append(student[0])
name.sort()

for names in name:
    print(names)



