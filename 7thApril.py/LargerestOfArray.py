n = input().split()
large = n[0]
for i in n: 
    a = int(i)
    if a > int(large) :
        large = a 
print(large)
