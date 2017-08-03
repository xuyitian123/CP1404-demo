str_1 = "This is a normal string."

str_2 = """

This

                 is

multiline

string

"""



str_3 = "This comes with escape characters. \nNext\t\tline." #\n for new line, \t for tab space \', \"

#print(str_3)



#print(ord('A')) #65 print the ordinal value associated with the character

#print(ord('a')) #97

#print(chr(65))



#for i in range(32, 101):

#    print("{} -> {}".format(i, chr(i)))

str_4 = "abcdefg"

str_5 = "0123456"

print(str_4[0]) #first character

print(str_4[3])

print(str_4[-3])

print(str_4[0:3]) #abc

print(str_4[0:7:2]) #print alternate characters, [start:end:step]

print(str_4[-3:-1])

print(str_4[:])

print(str_4[::-1])



"""

Given the string "abcdefghij", write code that will print the following:

1. 'jihgfedcba'

2. 'adgj'

3. 'igeca'

"""
test_str = "abcdefghij"
print(test_str[::-1])
print(test_str[::3])
print(test_str[-2::-2])

#test_str[1] = "z" #not allowed,immutable,cannot change the string partially
#test_str = "azghjg"#this is re-assignment
for each in test_str:
    print(each)

for index,value in enumerate(test_str):
    if value in "cz":
       print("{} -> {}".format(index,value))


print("w" in test_str)
print(len(test_str))

print(test_str.upper())
print(test_str.isupper())