import random

joke = ["Why did the tomato turn red? Because it saw the salad dressing!", "Why was the math book sad? Because it had too many problems."]

stop = True

while stop == True:
    print("Hey man, I`m your personal calculator! Select an operation: ")
    print("1. add")
    print("2. multiply")
    print("3. divide")
    print("4. subtract")
    print("5. tell a joke")
    print("6. exit")
    print()
    choice = input()
    print()
    
    print("OK you chose:",choice)
    print()

    if choice == "add":
        print("Enter first number: ")
        first_number = float(input())
        print("Enter second number: ")
        second_number = float(input())
        print("The result is:", first_number + second_number)
        stop = False
    elif choice == "multiply":
        print("Enter first number: ")
        first_number = float(input())
        print("Enter second number: ")
        second_number = float(input())
        print("The result is:", first_number * second_number)
        stop = False
    elif choice == "divide":
        print("Enter first number: ")
        first_number = float(input())
        print("Enter second number: ")
        second_number = float(input())
        print("The result is:", first_number / second_number)
        stop = False
    elif choice == "substract":
        print("Enter first number: ")
        first_number = float(input())
        print("Enter second number: ")
        second_number = float(input())
        print("The result is:", first_number - second_number)
        stop = False
    elif choice == "tell a joke":
        print("The result is:",random.choice(joke))
        stop = False
    elif choice == "exit":
        print("Buy Man")
        stop = False
    else:
        print("I don`t understand what do you want. Just try again")
        print()

