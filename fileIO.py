"""
# Writes to a file

name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()


# Appends to a file

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()


# Adds context manager

name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")


# Reads from a file, read is the default mode for open

with open("names.txt") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())

# Reads from a file, one line at a time

with open("names.txt") as file:
    for line in file:
        print("hello,", line.rstrip())


# Appends names to a list for sorting

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

# Reads a CSV file

with open("students0.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


# Unpacks a list

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

# Sorts a list of strings

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

# Reads a CSV file into a list of dict objects, creating empty dict first

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")



# Reads a CSV file into a list of dict objects, creating dict first

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")


# Reads a CSV file into a list of dict objects

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

for student in students:
    print(f"{student['name']} is in {student['house']}")

# Sorts a list of dictionaries using a function

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})


def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

# Sorts a list of dictionaries using a lambda function

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")


# Reads a CSV file using csv.reader

import csv

students = []

with open("students1.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

# Reads a CSV file using csv.DictReader

import csv

students = []

with open("students2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")



# Writes a CSV file using csv.writer

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students3.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])


# Writes a CSV file using csv.DictWriter

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

"""
# Opens and saves binary files

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)

# check this link: https://cs50.harvard.edu/python/2022/weeks/6/