cities=("BBSR", 'DELHI','MUMBAI')
print("BBSR" in cities)
print("MUMBAI" in cities)
print ("NEW_DELHI" in cities)

t = (12,34,56)
# t.append(12) # AttributeError: 'tuple' object has no attribute 'append'
my_list= list (t)
# print(my_list)
my_list.append(4)
t=tuple(my_list)
print (t)
my_list.append(7)
t1=tuple(my_list)
print(t1)
my_list.append(55)
t3=tuple(my_list)
print(t3)


# Similarly list can be converted to tuple
API_URLs=tuple(["abc.com", "fnp.com", "mmt.com"])
print(API_URLs)

tt=list()
print(tt)

