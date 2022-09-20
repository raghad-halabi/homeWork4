num1 = input("Enter the first number: ")
if num1.isdigit():
    print('''1 _ +
2 _ -
3 _ *
4 _ /
5 _ ^
6 _ % ''')
    operation = input("Choose the operator")
    num2 = input("Enter the second number: ")
    if num2.isdigit():
        if operation == "1" or operation == "+":
            result = int(num1) + int(num2)
        elif operation == "2" or operation == "-":
            result = int(num1) - int(num2)
        elif operation == "3" or operation == "*":
            result = int(num1) * int(num2)
        elif operation == "4" or operation == "/":
            result = int(num1) / int(num2)
        elif operation == "5" or operation == "^":
            result = int(num1) ^ int(num2)
        elif operation == "6" or operation == "%":
            result = int(num1) % int(num2)
        else:
            print("Error!!")
        print(result)
        print('''1. التقريب لأعلى رقم 
        2. أخذ الرقم بدون فاصلة عشرية 
        3. الخروج               ''')
        choose = input(" Choose: ")
        if choose == "1" or choose == "التقريب لأعلى رقم":
            result2 = result.__round__()
            print(result2)
        elif choose == "2" or choose == "أخذ الرقم بدون فاصلة عشرية":
            result2 = int(result)
            print(result2)
        elif choose == "3" or choose == "الخروج":
            pass
    else:
        print("Error!!")
else:
    print("Error!!")
