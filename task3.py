def main():
    scores = []
    for each in range(1, 6):
        message = "Enter value "+ str(each) + ":"#
        value = int(input(message))
        scores.append(value)
    print(scores)
    a = sorted(scores)
    print(a)
main()