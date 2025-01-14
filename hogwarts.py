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

students = [
    {'name': 'Harry', 'house': 'Gryffindor'},
    {'name': 'Draco', 'house': 'Slytherin'},
    {'name': 'Luna', 'house': 'Ravenclaw'},
    {'name': 'Hermonie', 'house': 'Gryffindor'},
    {'name': 'Ron', 'house': 'Gryffindor'},
]

for student in students:
    name = student['name']
    house = student['house']
    print(name, house, sep=' - ')