import csv

name = input("Enter your name: ")
town = input("Enter your home: ")
address = input("Enter your address: ")

name, town, address = name.capitalize(), town.capitalize(), address.capitalize()


with open('data_information.csv', 'a') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "town", "address"])
    writer.writerow({"name": name, "town": town, "address": address})