# secret_word = "what are you doing"
# x = secret_word.replace(" ","")
# print(x)
# print(len(x),'iterations, coming right up!')
# for i in x:
# #     print(i)
# s = 'garage'
# total = 0
# for char in s:
#     total + s.count(char)
#     print(total)
# print(total)

# text1 = input("Enter a text")
# if text1.isupper():
#     print(text1,"is uppercase")
# elif text1.islower():
#     print(text1,"is lowercase")
# elif text1.isdigit():
#     print(text1,"is digit")
# elif not text1.isalnum():
#     print(text1,"special")
# else:
#     print("its mix")

# letters = "*"
# digits = "123456789"
# for letter in letters:
#     for digit in digits:
#         print(letter + digit)


swaps = input()
ball_location = 1
for swap_type in swaps:
    if swap_type == 'A' and ball_location == 1:
        ball_location = 2
    elif swap_type == 'A' and ball_location == 2:
        ball_location = 1
    elif swap_type == 'B' and ball_location == 2:
        ball_location = 3
    elif swap_type == 'B' and ball_location == 3:
        ball_location = 2
    elif swap_type == 'C' and ball_location == 1:
        ball_location = 3
    elif swap_type == 'C' and ball_location == 3:
        ball_location = 1
    else:
        print("nothing")
print(ball_location)




















