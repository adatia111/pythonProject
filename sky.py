fileR = open("c:\\Users\Dipak\Documents\\sky.txt","r")
fileW = open("c:\\Users\Dipak\Documents\\sky3.txt","w")

data = fileR.read()
newdata=""
for x in data:
    if x=="a":
        newdata+="*"
    else:
        newdata+=x
fileW.write(newdata)


