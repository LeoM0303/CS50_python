students = []

with open('students.csv') as file:
    for line in file:
        name, home, adresses = line.rstrip().split(';')
        student = {"name": name, "home": home, "addresses": adresses }
        students.append(student)

for student in sorted(students, key = lambda student: student["name"]):
    print(f'{student["name"]} from {student["home"]} has addresses: {student["addresses"]}')