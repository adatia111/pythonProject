first=int(input("Enter First number:"))
last=int(input("Enter Last number:"))
i=first
total=0
totalOdd=0
totalEven=0
while i<=last:
    total=total+i
    if i%2==0:
        totalEven =totalEven +i
    else:
        totalOdd = totalOdd + i
    i=i+1
print("Sum Of All numbers:",total)
print("Sum Of All Even numbers:",totalEven)
print("Sum Of All Odd numbers:",totalOdd)
