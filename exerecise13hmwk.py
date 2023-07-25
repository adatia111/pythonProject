fileR = open("pelican.txt", "r")
data = fileR.read()
print(data)
list1 = data.split(" ")
print("Words: ", (len(list1)))
for i in list1:
    print(i.strip())  # The .strip function removes the whitespace