score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("The grade is: ", "A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score < 59 and score >= -1:
    print("F")
else:
    print("You are a super man")
