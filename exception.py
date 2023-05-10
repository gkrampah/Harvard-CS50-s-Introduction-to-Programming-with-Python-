"""
# Catches a ValueError

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

# Demonstrates a NameError

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")



# Demonstrates else

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    #use when you try and succeeded
    print(f"x is {x}")


# Adds a loop

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")

# Adds a loop

while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")
    

print(f"x is {x}")

# Adds functions, uses break and return


def main():
    x = get_int4()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

def get_int2():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x

def get_int3():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

def get_int4():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
"""
        
# Adds prompt

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()