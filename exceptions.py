listd=[12,45]

try:
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))
    print("shafeeq is back")
    print(listd[7])
    result = num1/num2
    print(".........................")

    print("the")
    print("result")
    print("of division")
    print("is")
    print(result)
    file2 = open("shafeeq.txt")
    data = file2.read()
    print(data)
except ZeroDivisionError:
    print("you cant divide by zero")
except IndexError:
    print("this location does not exist")
except FileNotFoundError:
    print("this file not exist")
print("today is monday")


