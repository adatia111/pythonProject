msg=input("enter any message:")
choice=input("what should i count:")
i=0
count=0
while i<len(msg):
    if msg[i]==choice:
        count+=1
    i+=1
print("you have entered",count)
