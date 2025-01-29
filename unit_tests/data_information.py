import csv

name = input("Enter your name: ")
town = input("Enter your home: ")
address = input("Enter your address: ")

name, town, address = name.capitalize(), town.capitalize(), address.capitalize()


with open('data_information.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow([name, town, address])