# Program: if age>18, allow to vote
# if age<18, not allwed for vote


user_age = int(input("Enter your age\n"))

if user_age > 18:
    print("You can vote")
else:
    print("You cant vote")
print("----------------------------")

#ternary
print("You can Vote" if user_age > 18 else "You cant vote")

print ("**************************************************")
print("You can Vote" if int(input("Enter your age\n")) > 18 else "You cant vote")


