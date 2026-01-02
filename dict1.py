names = ["Ajay","Mahavir","Mohit","Anushka"]
d = {}
for name in names:
    if name.startswith("M"):
        d[name] = len(names)
print(d)

names = ["Ajay","Mahavir","Mohit","Anushka"]
d = {name : len(names) for name in names if not name.startswith("M")}
print(d)

#if else condition:
name = "Ajay"
if name[0]=='A':
    print("vowel")
else:
    print("consonant")