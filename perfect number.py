number= int(input())
sum= 0
for i in range(1 , number):
    if number % i == 0:
        sum= sum + i
if (sum == number):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
