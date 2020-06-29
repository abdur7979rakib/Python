def add(x, y):
   return x + y

def sub(x, y):
   return x - y

def mult(x, y):
   return x * y

def div(x, y):
   return x / y

print("Select operation: ")
print("1.Add")
print("2.Sub")
print("3.Mult")
print("4.Div")

choice = input("Enter choice(1/2/3/4): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == '1':
   print(a,"+",b,"=", add(a,b))

elif choice == '2':
   print(a,"-",b,"=", sub(a,b))

elif choice == '3':
   print(a,"*",b,"=", mult(a,b))

elif choice == '4':
   print(a,"/",b,"=", div(a,b))
else:
   print("Invalid input")