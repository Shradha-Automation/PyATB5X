set1={7,6,5,7}
set2={4,4,3,2,5}
my_set=set1.union(set2)
print(my_set)

my_set=set1.difference(set2)
print(my_set)

my_set=set2.difference(set1)
print(my_set)

my_set=set1.intersection(set2) # intersection: common part
print(my_set)

my_set=set2.intersection(set1)
print(my_set)