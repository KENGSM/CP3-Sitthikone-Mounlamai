def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print(("Try again!!!"))
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input("Select the option number : "))
    if userSelected == 1:
        return vatCalculator()
    elif userSelected == 2:
        return priceCalculator()

def vatCalculator():
    price = int(input("Enter the price : "))
    vat = 7
    result = price + (price * vat / 100)
    print(result)
    return menuSelect()


def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    vat = 7
    price1n2 = price1 + price2
    print(price1n2 +(price1n2*7/100))
    return menuSelect()

print(login())