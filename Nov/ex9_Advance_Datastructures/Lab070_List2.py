my_list = [1,2,3]

# Indexing
print ("element at the index 0 - ", my_list[0])
print ("element at the index 1 - ", my_list[1])
print ("element at the index 2 - ", my_list[2])

# Append() # Append object to the end of the list
my_list.append(4)
my_list.append(5)
print (my_list)

# Extend() # Append a new List
my_list.extend([7,8,9])
print(my_list)

# insert()
my_list.insert(1, "shradha" )
my_list.insert(3,"priya")
print(my_list)

# remove()
my_list.remove(8)
my_list.remove('priya')
print(my_list)

my_list[3]="Sony" # insert name at index
print(my_list)

my_list. remove("Sony")
print(my_list)

print("-----------------------------------------")

# Copy
print(my_list.copy())
# or
my_list.copy()
print(my_list)

print(my_list.remove("shradha"))
print(my_list)

my_list[0]=78
print (my_list)

# Sort

my_list.sort()
print(my_list)

my_copy_list = my_list.copy()
print(my_copy_list)

