def main():
    centsperkwh = int(input("Enter cents per kWh"))
    dailyuse = int(input("Enter daily use in kWh"))
    numofbilling = int(input("Enter number of billing days"))
    estimatedfuel = centsperkwh * dailyuse * numofbilling
    print(estimatedfuel)
main()
