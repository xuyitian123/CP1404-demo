#file writting
string1="a,b,c,d"
output_file = open("data.txt","w")
output_file.write(string1)
output_file.close()

input_file = open("data.txt","r")
data = input_file.readlines()
for each in data:
    print(data)
input_file.close()