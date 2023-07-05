Belgium = 'Belgium:10445852 Brussels:737966 Europe:1830 Euro: Catholicism: Dutch: French: German:'

print(Belgium)
print("--------------------------------------------------------------------------------------")
msg=(Belgium)
i=0
word=""
while i<len(msg):
    if msg[i]==" ":
        print(word)
        word=""
    else:
        word+=msg[i]
    i+=1
print(word)
belpop = 10445852
brupop = 737966
print("population of Belgium plus Brussels is:",belpop+brupop)
