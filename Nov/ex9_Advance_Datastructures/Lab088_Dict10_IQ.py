# count number of vowels in a string

#input_string =input("Enter string eg: hello world\n")
#or
input_string = "hello world"
vowels = 'a,e,i,o,u'
vowels_count=0
for char in input_string:
    if char in vowels:
        vowels_count = vowels_count + 1
print(vowels_count)
