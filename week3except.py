filename = str(input("Enter a filename:"))
try:
    my_name = open(filename,"r")#problematic code
    print(my_file.readlines())
    x = 9 + "a"
    my_file.close()
except FileNotFoundError:
    print("File not found.")
except TypeError:
    print("Type mismatch.")
except :#generic except
    print("File not found.")