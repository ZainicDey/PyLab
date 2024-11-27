n = int(input('How many students?:'))
students = []
for i in range(0,n):
    print(f'student no{i+1} details:')
    name = input('name:')
    id = input('id:')
    age = input('cgpa:')

    student = {
        "name" : name,
        "id": id,
        "age": age
    }

    students.append(student)

print(students)
