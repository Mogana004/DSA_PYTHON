N= int(input())
N1= str(N)
K= len(N1)
sum= 0
for i in N1:
    digit = int(i)
    sum= sum+ digit** K
print(sum)
    
//given a number N  , write a program to print the sum of the Kth power of all the digits in the given number , k indicates the number of digits of the number N
