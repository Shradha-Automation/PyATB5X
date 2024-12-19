# Tuple (Collection of Items)
# Immutable
from selenium.webdriver.common.devtools.v125.page import print_to_pdf

my_tuple = (1,2,3,4,5)
print(my_tuple)
# my_tuple [0]=54 # Tuple does not suport item assignment

# Real case, tuples
my_tuples = ("https://shradha.com", "https://Mad.com", "https://Sam.com")
my_API_List = list(my_tuples)
print(my_tuples)
print (my_API_List)
# my_tuple[0]= "abc.com" # TypeError: 'tuple' object does not support item assignment

print(my_tuples[0])
print(my_tuples[1])
print (my_tuples[2])
