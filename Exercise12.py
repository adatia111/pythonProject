cheese=["cheddar","stilton","cornish-yarg"]
cheese.append("Oke")
print(cheese)
while True:
    name=input("add new cheeses:")
    if name=="":
        break
    cheese.append(name)
print("...............................")
print(len(cheese),"in the cheese list")


i=0
while i<len(cheese):
            print(cheese[i])
            i+=1






