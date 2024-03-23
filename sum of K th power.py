N= int(input())
N1= str(N)
K= len(N1)
sum= 0
for i in N1:
    digit = int(i)
    sum= sum+ digit** K
print(sum)
    
