age = int(input("Enter your age: "))
if age <= 18:
    print("you are younger")
elif age > 18 and age <= 60 :
    print("you are elder")
elif age > 60 and age <= 90:
    print("you are old")
else :
    print("Expire")
