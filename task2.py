def multiply(num):
    for i in range(11):
        #0 * 5 = 0
        print("{} * {} = {}".format(i,num,i*num))
multiply(15)

def multiply_while(num):
    count = 10
    while count >= 0:
        print("{}*{}={}".format(count,num,count*num))
        count -= 1 #count = count - 1
multiply_while(100)