number = input()
list = number.split()
div_3 = []
for n in list :
    n= int(n)
    if n % 3 == 0 :
        div_3 += [n]
print(div_3)
