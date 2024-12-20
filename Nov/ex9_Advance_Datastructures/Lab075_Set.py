# SET: Modifiable(add,remove,update,delete) but not Mutable
# Collection of unique elements (Remove duplicates)
# {}

list_of_unique_items = {1,2,3,7,8,3,4, 4,5,6,7}
print(list_of_unique_items)

list1=[7,8,6,5, 1,2,3,3,3,2,4,5,6,7]
set1=set(list1)
print(set1) # No order
list2=[33,2,45.6,7,8,88,7,2]
set2=set (list2)
print(set2)

t=["GOD","MAA","MAA"]
print(set(t))