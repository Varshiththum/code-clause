def calculator():
    choice=input()

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

 
    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        result = num1 / num2
    elif choice == '5':
        result = num1 % num2
    elif choice == '6':
        result = num1 // num2
    else:
        print("Invalid input")
        return

   
    print(result)


calculator()