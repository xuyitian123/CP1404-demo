score = float(input("Enter score:"))
if score < 0:
    print("Invalid score")
else:
    if score > 50:
        print("Passable")
    if score > 90:
        print("Excellent")
    if score > 100:
        print("Invalid score")
    if score < 50:
        print("Bad")