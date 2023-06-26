pin = {1234}

count = 1

while True:
    enter_pin = int(input("enter your pin:"))
    if (enter_pin)in pin:
        print("")
        print("correct pin")
        print("")
        print("welcome to your banking")
        break
    print("")
    print("incorrect pin.please try again")
    print()
    count += 1
    if count == 4:
        print("incorrect pin entered 3 times")
        break
