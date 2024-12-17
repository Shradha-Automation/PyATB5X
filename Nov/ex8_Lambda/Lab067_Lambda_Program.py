# Write a program to calculate even and odd

def even_or_odd (num):
    if num % 2 == 0:
        print ("Even")
    else:
        print ("Odd")

even_or_odd(6)
even_or_odd(57)

n=int(input("Enter a number\n"))
Check_Even_or_Odd = lambda num: "Even" if num % 2 ==0 else "Odd"
print (Check_Even_or_Odd(n))

# print (Check_Even_or_Odd (56))