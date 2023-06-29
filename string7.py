msg=input("enter any message:")
find=input("what are you looking for:")
i=0
count=0
print("..........................................................")
while i<len(msg):
    if msg[i]==find[0]:
        if msg[i:i+len(find)]==find:
            count+=1
    i+=1
print(count,find,"are found")
