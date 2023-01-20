import sys 
import random

#print("First argument:",sys.argv[1:])
#print("First argument:", sys.argv[1])

joke = ["Why did the tomato turn red? Because it saw the salad dressing!", "Why was the math book sad? Because it had too many problems."]

command = str(sys.argv[1])

stop = True
while stop == True:
    print("OK you chose:",command)
    print()
    
    if command == "add":
        first_number = float(sys.argv[2])
        second_number = float(sys.argv[3])
        print("The result is:", first_number + second_number)
        stop = False
    elif command == "multiply":
        first_number = float(sys.argv[2])
        second_number = float(sys.argv[3])
        print("The result is:", first_number * second_number)
        stop = False
    elif command == "divide":
        first_number = float(sys.argv[2])
        second_number = float(sys.argv[3])
        print("The result is:", first_number / second_number)
        stop = False
    elif command == "subtract":
        first_number = float(sys.argv[2])
        second_number = float(sys.argv[3])
        print("The result is:", first_number - second_number)
        stop = False
    elif command == "tell a joke":
        print("The result is:",random.choice(joke))
        stop = False
    elif command == "exit":
        print("Buy Man")
        stop = False
    else:
        print("I don`t understand what do you want. Just try again")
        print()
        stop = False
        