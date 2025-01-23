# students = ['Harry', 'Ron', 'Hermione', 'Neville', 'Ginny']

# for i in range(len(students)):
#     print(i + 1, students[i])

# students = {
#     'Harry' : 'Gryffindor',
#     'Draco' : 'Slytherin',
#     'Luna' : 'Ravenclaw',
#     'Hermonie' : 'Gryffindor',
#     'Ron' : 'Gryffindor',
# }

# for student in students:
#     print(student, students[student])

def display_students():
    students = [
        {'name': 'Harry', 'house': 'Gryffindor'},
        {'name': 'Draco', 'house': 'Slytherin'},
        {'name': 'Luna', 'house': 'Ravenclaw'},
        {'name': 'Hermione', 'house': 'Gryffindor'},
        {'name': 'Ron', 'house': 'Gryffindor'},
    ]

    for student in students:
        print(f"{student['name']} {student['house']}")

if __name__ == "__main__":
    display_students()
