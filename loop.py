name = "ajay singh"
name2 = ""
for c in name:
    name2 += c.upper()
print(name2)


number = [1,2,3,4,5,6]
s = 0
for n in number:
    s += n
print(s)

#length of all string
names = ["ajay singh","mahavir","mohit","anushka"]
d = {}
for name in names:
    d[name] = len(name)
print(d)

d = {}
d["mahavir"] = 9
d["james"] = 5
print(d)

names1 = ["Ajay","mahavir","Mohit","Anushka"]
d = {name : len(name) for name in names1}
print(d)

