maximum = int(input("enter the maximum value:"))
even_total = 0
odd_total = 0
numbers: int
for number in range(1,maximum + 1):
    if number % 2 == 0:
        even_total = even_total + number
    else:
        odd_total = odd_total + number

print("the sum of even numbers from 1 to {0} = {1}".format(number,even_total))
print("the sum of odd numbers from 1 to {0} = {1}".format(number,odd_total))




