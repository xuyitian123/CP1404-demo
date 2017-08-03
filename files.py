out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)  #
out_file.close()

# Quick Program 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()


in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1)
print(number2)
print("The total of the number is ",number1+number2)
in_file.close()
