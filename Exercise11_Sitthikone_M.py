numberOfRow = int(input("Enter the number of row : "))

for x in range(numberOfRow):
    print(" " * (numberOfRow - x), "*" * (((x+1)*2) -1 ))