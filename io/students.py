import csv

students = []

with open('students.csv') as file:
    reader = csv.reader(file)
    for name, home, addresses in reader:
        students.append({"name": name, "home": home, "addresses": addresses})

for student in sorted(students, key = lambda student: student["name"]):
    print(f'{student["name"]} from {student["home"]} has addresses: {student["addresses"]}')