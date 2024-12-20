set1=set([1,2,3,4,5,5,4,3,2,1])
print(set1)
print(len(set1))

for i in set1:
    print(i)

set1.add("Shradha")
set1.add("Shradha") # it will add only once as no duplicates are allowed.
print(set1)