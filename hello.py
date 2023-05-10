# Ask user for their names
#name = input('what is your name? ').strip().title()
#name = name.strip().capitalize()
#remove whitespace on the side adnd capitalize first letter ofevery word 
#name = name.strip().title()

# split user name into last and first
#first, last = name.split(" ")
# say hello to user
#print(f'hello {first}!!!!')
#print(f'hello ' +name+'!!!!')
#print('hello', name, '!!!')
#print('hello ', end='')
#print(name)
#print('hello, "friend"')
# print('hello, \'friend\'')

#hello()   This will result in an error because the function is defined below
"""
def main():
    hello('David')

def hello(to="world"):
    print('hello, '+ to)


#hello()   
#main2()

def main2():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n
"""
def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"

if __name__ =='__main__':
    main()