employee_name = input("enter employee name:")
employee_salary = input("enter salary:")


tax = int(employee_salary) * 21/100
net_salary = int(employee_salary) - tax

print("employee name:",employee_name)

print(employee_name+"'s",employee_salary)

print(".......................................................")

print("tax calculated:",tax)
print("net salary:",net_salary)

print(".........................................")
