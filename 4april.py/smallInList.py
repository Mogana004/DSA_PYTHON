numbers =input()
list = numbers.split()
s = int(list[0])
for num in list :
    num = int(num)
    if num <s :
        s = num 
print(s)
