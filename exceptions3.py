def division(a,b):
    print("you have called function")
    result = a/b
    print("the result of")
    print("division is:",result)



print(".........................................................")
print("the division process:")

try:
    division(4,0)
except ZeroDivisionError:
    print("tried to divide a number by zero")
print("every thing completed.")
