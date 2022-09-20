print("Welcome to our program")
name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")

if type(name) == str and name.isdigit():
    if age.isdigit():
        print("Hello Mr/Ms " + name + " age " + age + " located in " + address + '''.
    thanks for being one of our community,    enjoy''')
    else:
        print("Error!!")

else:
    print("Error!!")