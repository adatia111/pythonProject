file1 = open("pelicans.txt","w")
file1.write("A wonderful bird is the pelican,")

fileW= open("c:\\Users\Dipak\Documents\\pelicans.txt","a")
fileW.writelines(["A wonderful bird is the pelican,\n", "His bill holds more than his belican,\n", "He can take in his beak,\n", "Enough food for a week,\n", "But i'm damned if i see how the helican.\n"])
fileW.close()


