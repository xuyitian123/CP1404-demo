def main():
    number = int(input("Enter the number:"))
    if number >= 1 and number <= 50 and number%3==0 and number%5==0:
        print("FizzBizz")
    elif number >= 1 and number <= 50 and number%3==0:
        print("Fizz")
    elif number >= 1 and number <= 50 and number%5==0:
        print("Buzz")
    else:
        print("Invalid")
main()
