keys = ["name", "role","experience"]
values = ["Shradha", "SDET", 7]
my_dict=dict(zip(keys,values))
print(my_dict)




# Merge 2 dictionary

dict1 = {"a" : 1, 'b':2}
dict2 = {"c": 3, 'd':4, 'b':3, 'a':7}
merged_dict= dict1 | dict2
print(merged_dict.get("a"))
