#Make a calculator
#Add
def add(x, y):
    return x + y
#Subtract
def subtract(x, y):
    return x - y

#Multiply
def multiply(x, y):
    return x * y

#Divide
def divide(x, y):
    return (x / y)


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1 + num2))
    elif choice == '2':
        print(num1,"-",num2,"=")
    elif choice == '3':
        print(num1,"*",num2,"=")
    elif choice == '4':
        print(num1,"/",num2,"=")

    next_calcultion == input("")
    if next_calculation == "no":
        break
    else:
        print("Invalid input")