# Dict:
#.Undefined, Mutable, and indexed collection of Key and Value Pairs in Python
#. Defined using curly braces {}

my_dict = {
    "name": "Aman",
    "Age": 34,
    "Role": "SDET",
    "Experience": 3
}

print(my_dict)

my_dict ["name"]=="Shradha"
print(my_dict)

del my_dict['Role']
print(my_dict)

for key,value in my_dict.items():
    print(key,"=" ,value)

print("Age" in my_dict)
print("Role" in my_dict)

