import math

def give_me_power(num):
    return math.pow(num,2)
op = give_me_power(7)
print (op)

op = lambda: math.pow(int(input("Enter num\n")),2)
print (op())