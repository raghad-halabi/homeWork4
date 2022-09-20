numbers = []
while numbers.__len__() < 5:
    counter = input("Enter new number: ")
    numbers.append(counter)
print(numbers)
print("max number: " + max(numbers))
print("min number: " + min(numbers))