def getpassword():
    password = input("Enter a password:")
    return password
def encodepassword(password):
    for i in password:
        asciNum=ord(i)