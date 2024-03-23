m= int(input())
n= int(input())
list = []
for i in range(m , n+1):
    if (i % 6 == 0):
        list.append(i)
if (len(list)>0):
    print(*list)
else:
    print("No Numbers Found")



