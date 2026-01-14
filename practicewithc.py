# x = 10
# y = 15
# if x%2 ==y%4:
#     print("Both are equal")
# else:

# c = int(input("Enter cost price"))
# s = int(input("selling price"))
# if c > s:
#     print(c-s)
#     print("you are in loss")
# elif c < s:
#     print(s-c)
#     print("you are in profit")
# else:
#     print("Equal")

ent = input("Enter your value: ")
if 65 <= ord(ent) and ord(ent) <= 90:
    print(ent,"This a capital letter")
elif ord(ent) >= 97 and ord(ent) <= 122:
    print(ent,"This a lower letter")
elif ord(ent) >= 48 and ord(ent) <= 57:
    print(ent,"This a numeric value")
else:
    print(ent,"This a special character")


