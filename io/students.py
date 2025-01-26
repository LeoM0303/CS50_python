with open('students.csv', 'r') as file:
    for line in file:
         row = line.rsplit().split(",")