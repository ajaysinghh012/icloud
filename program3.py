# r = int(input("what is radius"))
# h = int(input("what is height"))
# pie = 3.14
# x = (pie*(r**2)*h )/3
# print(x)
# i = 1
# while i <= 10:
#     print(i)
#     i = i +1

# x = 2
# while x == 1:
#     x = x -1
#     print(x)

# x = 2
# for x in range(2,):
#     print(x)

num = int(input("Enter a number: "))

if num == 0 or num == 1:
    print("Prime")

i = 2
while i < num:
    if num % i == 0:
        print(f"Not prime - divisible by {i}")
        break
    i = i + 1

if i == num:
    print("Prime")











