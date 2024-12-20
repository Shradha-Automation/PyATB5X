# Task
# Sort a dictionary by its value in descending order
my_dict= {'a': 3, 'b':4,'c':1}
# o/p: (c:1, a:3. b:4)

# function that returns a maximum value from a dictionary
# a=10, b=20, c=30

def max_value_dict(dictionary):
    return max(dictionary.values()) # list of values

print(max_value_dict({'a':10,'b':20,'c':30}))

def min_value_dict(dictionary):
    return min(dictionary.values()) # list of values
print(min_value_dict({'a': 10, 'b': 20, 'c': 30}))

