while True:
    print("welcome to my calculator")
    print("Options")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiplay' to multiplay two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program/n")
    x=input("enter:")
    if x=="quit":
        print("exit")
        break;
    elif x=="add":
        n1=float(input("please enter a number1:"))
        n2=float(input("please enter a number2:"))
        result=n1 + n2
        print(result)
    elif x=="subtract":
        n1=float(input("please enter a number1:"))
        n2=float(input("please enter a number2:"))
        result=n1 - n2
        print(result)
    elif x=="multiplay":
        n1=float(input("please enter a number1:"))
        n2=float(input("please enter a number2:"))
        result=n1 * n2
        print(result)
    elif x=="divide":
        n1=float(input("please enter a number1:"))
        n2=float(input("please enter a number2:"))
        result=n1 / n2
        print(result)
