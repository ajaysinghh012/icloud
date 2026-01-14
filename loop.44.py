# name = "jahaj"
# l = 0
# r = len(name) - 1
# if name[l] == name[r] and name[l+1] == name[r-1] and name[l+2] == name[r-2] and name[l+3] == name[r-3]:
#     print("yes is is a name palindrome")
# else:
#     print("no")

name = "malayala"
l = 0
r = len(name) - 1
flag = True
for i in range(len(name) // 2):
    if name[l] != name[r]:
        flag = False
        break
    l += 1
    r -= 1

if flag:
    print("its palindrome")
else:
    print("its not palindrome")
