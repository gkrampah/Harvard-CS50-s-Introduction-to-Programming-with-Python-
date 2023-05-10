"""
x = int(input("What's x? "))
y = int(input("What's y? "))
if x < y:
    print( 'x is lesser than y')

if x > y:
    print( 'x is greater than y')

if x == y:
    print('x is equal to y')



x = int(input("What's x? "))
y = int(input("What's y? "))
if x < y:
    print( 'x is lesser than y')

elif x > y:
    print( 'x is greater than y')

else:
    print('x is equal to y')


x = int(input("What's x? "))
y = int(input("What's y? "))
if x < y or x>y:
    print( 'x is not equal to y')
else:
    print('x is equal to y')


x = int(input("What's x? "))
y = int(input("What's y? "))
if x != y:
    print( 'x is not equal to y')
else:
    print('x is equal to y')


x = int(input("What's x? "))
y = int(input("What's y? "))
if x == y:
    print( 'x is equal to y')
else:
    print('x is not equal to y')


score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

score = int(input("Score: "))

if 90 <= score and score <= 100:
    print("Grade: A")
elif 80 <= score and score < 90:
    print("Grade: B")
elif 70 <= score and score < 80:
    print("Grade: C")
elif 60 <= score and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

score = int(input("Score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")


score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# Demonstrates modulo operator

x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# Demonstrates a function that returns a bool


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_even(n):
    return True if n % 2 == 0 else False

def is_even(n):
    return n % 2 == 0

main()


# Compares multiple strings with if/elif/else

name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# Uses or

name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
"""

# Uses |

name = input("What's your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")