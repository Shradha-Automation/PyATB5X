from Nov.ex9_Advance_Datastructures.Lab070_List2 import my_list

cities=("BBSR", 'DELHI','MUMBAI')
print("BBSR" in cities)
print("MUMBAI" in cities)
print ("NEW_DELHI" in cities)

t = (12,34,56)
t.append(12) # AttributeError: 'tuple' object has no attribute 'append'
my_list= list (t)
print (my_list)