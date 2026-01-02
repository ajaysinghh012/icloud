def calculate(l1, l2, op):
   if op == "+":
      print(l1+l2)
   elif op == "-":
      print(l1-l2)
   elif op == "*":
      print(l1*l2)
   elif op == "/":
      print(l1/l2)
   else :
      print("error")

while True:
   num1 = int(input("enter first number"))
   num2 = int(input("enter second number"))
   op = input("enter operation")
   calculate(num1,num2,op)