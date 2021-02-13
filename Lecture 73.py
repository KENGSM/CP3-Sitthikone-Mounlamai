systemMenu = {"Coke":20,"Water":10,"Beer":30}
menuList = []
def showBill():
    print("---- My Food ----")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        total += int(menuList[number][1])
    print("---- *** ----")
    print("Total Price : ", total , "THB")

while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

showBill()

