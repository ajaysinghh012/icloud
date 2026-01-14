

parking = int(input("Enter parking spot number"))
yesterday = input("parking space")
today = input("today space")

occupied = 0
for i in range(parking):
    if yesterday[i] == "C" and today[i] == "C":
        occupied +=1
    else:
        print("Not occupied")
print(occupied)