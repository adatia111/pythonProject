class  skyabsentiesException(Exception):
    pass

def salarySlip(name,salary,absenties):
    if absenties>5:
        Exp = skyabsentiesException()
        raise Exp
    if salary>=2000:
        tax = salary* 21/100
    else:
        tax = salary*15/100
    net = salary - tax
    print("name:",name)
    print("tax calculated is:",tax)
    print("net salaryis:",net)

def HR():
    try:
        salarySlip("shafeeq",2100,7)
    except skyabsentiesException:
        print("sorry too many absenties")

def IT():
    try:
        salarySlip("shafeeq",2100,7)
    except skyabsentiesException:
        print("that is fine they were in the office for 24 hours")

IT()

