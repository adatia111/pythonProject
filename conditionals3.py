
uniquewords = []
def isItUnique(checkword):
    i=0
    while i<len(uniquewords):
        if uniquewords[i]==checkword:
            return False
        i+=1
    uniquewords.append(checkword)
    return True

def messageprocessing(message):
        i=0
        newmessage=""
        words=""
        while i<len(message):
            if message[i]==" ":
                if isItUnique(words)==True:
                    newmessage+=words+" "
                words=""
            else:
                words+=message[i]
            i+=1
        if isItUnique(words)==True:
            newmessage+=words+" "
        print(newmessage)

msg=input("enter any message:")
messageprocessing(msg)



