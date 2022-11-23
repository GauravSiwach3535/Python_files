# Salary and service.
salary = int(input("What is your salary: "))
service = int(input("How many years of service: "))

if service > 10 :
    print(salary + 10%salary)

elif service > 5 :
    print(salary + 5%salary)

elif service < 5 :
    print(salary + 3%salary)

else:
    print("no bonus")