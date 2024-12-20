# Frequency of characters in a string

string ="automation"
string = input("Enter the input eg: automation")
char_count= {}

for char in string:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)