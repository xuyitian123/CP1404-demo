def stars(num):
     astericks = "*" *20
     print(astericks)
stars(20)
def name():
    length=len(name)
    halflength=int(length/2)
    return name
def main():
    name = input("Type in your sentense:")
    stars(20)
    length = len(name)
    halflength = int(length / 2)
    print(name[0:halflength])
    print(name[halflength: length])
    stars(20)
main()