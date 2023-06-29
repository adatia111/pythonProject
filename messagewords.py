msg = input("enter any message:")
i = 0
word=""
while i<len(msg):
    if msg[i]==" ":
        print(word)
        word=""
    else:
        word+=msg[i]
    i+=1
print(word)