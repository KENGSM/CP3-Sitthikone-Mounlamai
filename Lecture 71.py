menuList = []
priceList = []

def showBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])

def totalPrice():
    print("---- *** ----")
    total = 0
    for i in list(priceList):
        total += int(i)
    print("Total Price : ", total, "THB")

while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append((menuPrice))


showBill()
totalPrice()