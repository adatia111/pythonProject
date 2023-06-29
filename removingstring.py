msg = input("enter any message:")
what = input("remove which character:")
newmsg =""
i = 0
while i<len(msg):
    if msg[i]!=what:
        newmsg+=msg[i]
    i+=1
print("new message:",newmsg)
