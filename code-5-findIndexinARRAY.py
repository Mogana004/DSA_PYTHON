def find_element(A , K ):
    for i in range(len(A)):
        if A[i] == K:
            return  i 
    return -1 
            
N= int(input())
A= list(map(int, input().split()))
K= int(input())
find= find_element(A , K)
print(find)
