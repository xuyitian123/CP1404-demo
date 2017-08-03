"""
Write a program that asks the user for their age and then prints whether it is odd or even.
The program should not crash if the user enters a non-number
The program should not allow an invalid age number
Re-prompt until a valid number is entered
"""
def get_age()
 while True:
   try:
    age = int(input("enter your age:"))
    if age < 0 or age > 120:
        print("Age out of range.")
    else:
        print("Age accepted.")
        break
    except ValueError:
      print("Enter a numberic number.")
get_age()