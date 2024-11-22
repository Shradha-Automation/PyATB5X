# Write a python program to calculate the area of a circle given its radius using formula
# area=pi4^2 (Take pie as 3.14)

# Logic Building Formula

# // Step 1: //
# Figure out the inputs and output
# input -> r -> data type -> float
# pi = 3.14
# power ->pow or ** ->  any
# o/p -> float area, print area

# // Step 2: //
# rough logic: area = 3.14 * pow (r, 2)

# // Step 3 //
radius = float(input("Enter radius of the circle\n"))
print(radius)
area = 3.14 * (radius ** 2)
print(f"Area of the circle {area}")  # formatting is basically give you format
# or
print(f"Area of the circle {area:.3f}")
# or
print("Area of the circle:", area)

# or
print (3.14 * (float(input("Enter the radius of the circle\n")))**2)
# or
"""import math

print(math.pi)
print(math.pow(radius, 2))
area = math.pi * math.pow(radius, 2)
print("Area of the circle:", area) """

