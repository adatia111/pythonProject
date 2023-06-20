name=input("enter employee name:")
salary=int(input("enter employee salary:"))

if salary>=1000:
    if salary>=2000:
        tax = salary * 21/100
    else:
        tax = salary * 15/100
else:
    tax = 0
net=salary-tax
print(".....................................................")
print("tax calculated:",tax)
print("net salary:",net)








