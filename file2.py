file1=open("students.txt","w")
print("please enternames 10 student:")
i=1
while i<=10:
    print("number",i)
    name=input("enter name:")
    file1.write(name+" ")
    file1.write(",")
    file1.write("\n")
    i=i=i+1

