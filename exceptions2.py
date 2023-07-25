listd=[12,45]

try:
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))
    print("shafeeq is back")
    print(listd[1])
    result = num1/num2
    print(".........................")
    print("result",result)
    print("..........................")
    file2=open("a2.txt")
    data = file2.read()
    print(data)



except ZeroDivisionError:
    print("you cant divide by zero")
except IndexError:
    print("this location does not exist")
except FileNotFoundError:
    print("this file not exist")
finally:
    print(".........done.......")

print("today is monday")