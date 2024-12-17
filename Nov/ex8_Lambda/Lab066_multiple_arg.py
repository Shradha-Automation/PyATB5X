def add (a,b):
    return a+1, b+2
result = lambda a, b : (a+1, b+2)
print (result (5, 2))

def mul (a,b):
    return a * b
result = lambda a,b : a*b
print (result (7,3))

def sum (a, b, c):
    return a+b+c
result = lambda a, b, c : a+b+c
print (result(2,5,4))