def convert(num):
    answer=""
    if num>=1000:
        answer =  ones(int(num/1000)) +" Thousand"
        num = num % 1000
    if num>=100:
        answer =  answer+ ones(int(num/100)) + " Hundred"
        num = num % 100
    if num>=20:
        answer = answer + ty(int(num/10)*10)
        num = num % 10
    if num >=1:
        answer = answer + ones(num)
    return answer
i=1
while i<=3000:
    print(i,"=",convert(i))
    i=i+1