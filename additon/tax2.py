def tax(salary):
    tax = salary * 19.50 / 188
    return tax


salary = int("enter salary:")
net = salary - tax(salary)
print()
