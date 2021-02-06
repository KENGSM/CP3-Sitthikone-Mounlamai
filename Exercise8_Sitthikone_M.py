print("")
print("--------***--------")
print("Please Log in your ID")
print("--------***--------")
print("")
id = (input("Enter your ID : "))
pw = (input("Enter your password : "))

if id == "kengsm" and pw == "123123":
    print("==== Welcome to Our Shop====")
    print("::: Select the Item ::: ")
    print("")
    print("----------------")
    print("1. Coke 15 THB")
    print("2. Cake 40 THB")
    print("3. Water 10 THB")
    print("----------------")
    print("")
    userselection = int(input("Enter number of item : "))
    print("")
    if userselection == 1:
        cokePrice = 15
        print("#You Have Selected Coke#")
        unit = int(input("Please Select the amount : "))
        print("")
        print("----------------")
        print("Coke", unit, "unit")
        result = cokePrice * unit
        print("Total Price = ", result, "THB")
        print("----------------")
    if userselection == 2:
        cakePrice = 40
        print("#You Have Selected Cake#")
        unit = int(input("Please Select the amount : "))
        print("")
        print("----------------")
        print("Cake", unit, "unit")
        result = cakePrice * unit
        print("Total Price = ", result, "THB")
        print("----------------")
    if userselection == 3:
        waterPrice = 10
        print("#You Have Selected Water#")
        unit = int(input("Please Select the amount : "))
        print("")
        print("----------------")
        print("Water", unit, "unit")
        result = waterPrice * unit
        print("Total Price = ", result, "THB")
        print("----------------")




