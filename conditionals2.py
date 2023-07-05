trainers=[]

while True:
    name=input("enter trainer name:")
    if name=="":
        break
    trainers.append(name)
print("...............................")
print(len(trainers),"trainers work in QA")
i=0
while i<len(trainers):
            print(trainers[i])
            i+=1



