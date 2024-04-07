s= input().split(" ")
sum= 0 
for i in range( 0 , len(s)):
    sum= sum + int(s[i])
    avg = sum/len(s)
print(round(avg, 2))
