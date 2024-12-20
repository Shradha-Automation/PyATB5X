# Remove duplicate values  from a dictionary

my_dict={'a':10,'b':20,'c':30, 'a':100,'b':20,'c':30}
# o/p= remove duplicates
unique_value = set() # empty set keep only the unique value

result = {}
for key, value in my_dict.items():
    if value not in unique_value:
        result[key]= value
        unique_value.add(value)
print(result)
