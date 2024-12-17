num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))

if num1>num2 and num1>num3:
    print("The maximim number is: ", num1)
elif num2>num1 and num2>num3:
    print("The maximum number is: ", num2)
elif num3>num1 and num3> num2:
    print("The maximum number is: ", num3)
else:
    print("Not a valid input")
