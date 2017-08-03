string1="a,b,+c,d"
split_data = string1.split(",")#split according to comma
print(string1)
print(split_data)
print(split_data[1])

#alignment of string format
greet = "How are you?"
name = "John"
day = "Monday"
num = 99.8889678
now_str = "{:>50s},{}?\n Good{},number is ${:.2f}".format(greet,name,day,num)
print(new_str)