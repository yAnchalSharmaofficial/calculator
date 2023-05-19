#calculator

a=int(input("Enter your first number: " ))
print("Operation available:\nAddition(+)\nSubtraction(-)\nMultiplication(*)\nDivision(/)\nFloor Division(//): To get value without fraction\nExponential value(**)\nModulus(%): To get remainder only")
b=input("Enter your operator: ")
c=int(input("Enter your second number: "))
if b == "+":
  print("Result is",a+c)
elif b == "-":
  print("Result is",a-c)
elif b == "*":  
  print("Result is",a*c)
elif b == "/":
  print("Result is",a/c)
elif b == ("//"):
  print("Result is",a//c)
elif b == "%":
  print("Result is",a%c)

elif b == "**":
  print("Result is",a**c)
else:
  print("invalid operatiom")
