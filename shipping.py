item = int(input("Number of items:"))
while item < 0:
    print("Invalid choice,please try again")
    item = int(input("Number of items:"))

if item > 0:
        totalprice = 0
        totalitem = item
        for item in range(item):
            price = float(input("Price of item:"))
            totalprice = totalprice + price
            if totalprice > 100.00:
               totalprice = totalprice * 0.9
        print("Total price for {} is ${:2f}".format(totalitem,totalprice))
