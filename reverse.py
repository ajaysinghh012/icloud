# num = int(input("Enter a number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# num4 = int(input("Enter 4th number: "))
# num5 = int(input("Enter 5th number: "))
#
# if num2 == num4 and num == num5 :
#     print("Number are equal")
# else:
#     print("Number are not equal")

num = int(input("Enter 5 digit number"))
for i in range(num):
    digit_1 = num % 10
    print(digit_1)
    num = num // 10
print(i)


# digit_2 = num%10
# print(digit_2)
# num = num // 10
#
# digit_3 = num%10
# print(digit_3)
# num = num // 10
#
#
# digit_4 = num%10
# print(digit_4)
# num = num // 10
#
# digit_5 = num%10
# print(digit_5)
