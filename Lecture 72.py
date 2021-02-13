menuList = []
def showBill():
    print("---- My Food ----")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number])
        total += int(menuList[number][1])
    print("---- *** ----")
    print("Total Price : ", total , "THB")


while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName, menuPrice])

showBill()

