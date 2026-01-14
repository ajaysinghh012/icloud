# game = 'Lost Vikings'
# print(game[2:-6])
# valid = False
# while not valid:
#     s = input()
#     valid = len(s) == s and s[:2] == "x,y"

# s = "zephyrajaysingh"
# for i in range(0,len(s),3):
#     print(s[i])
# for i in range(len(s)-1,-1,-1):
#     print(s[i])

# s = 'zephyr'
# i = 0
# while i <len(s):
#     print("We have Z" + s[i])
#     i = i + 1

s = 'zephyr'
i = 0
while i < len(s):
    if s[i] == 'p':
        break
    print(s[i])
    i = i + 1
