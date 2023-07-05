charachter=input("enter any alphabet:")

if ord(charachter)>=65 and ord(charachter)<=90:
    print("you have entered uppercase")
    print(chr(ord(charachter)+32))

if ord(charachter)>=97 and ord(charachter)<=122:
    print("you have entered lowercase")
    print(chr(ord(charachter)- 32))
