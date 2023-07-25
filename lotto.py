import random


a = list(range(1,50))
print(a)
lottodip = []

for i in range(6):
    lottodip.append(random.choice(a))
print("random lottery numbers generated are:",lottodip)



