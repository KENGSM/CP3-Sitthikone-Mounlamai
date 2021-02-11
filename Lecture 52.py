totalPrice = int(input("Enter the total price : "))

def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return int(result)

print(vatCalculate(totalPrice))