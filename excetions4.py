class skyabsentiesexception(Exception):
    pass

def salaryslip(name,salary,absentism):

    if absentism>5:
        exp= skyabsentiesexception()
        raise exp
    if salary>=2000:
        tax = salary*20/100
    else:
        tax = salary * 15/100
    net = salary - tax
    print("name:",name)
    print("tax calculated is:",tax)
    print("net salary is:",net)

try:
    salaryslip("dipak",7000,0)
except skyabsentiesexception:
    print("sorry to many absenties")





