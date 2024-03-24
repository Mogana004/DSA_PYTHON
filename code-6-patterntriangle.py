def print_triangle(N):
    for i in range( 1 , N+1):
        for j in range( N-i):
            print(" " , end="")
        for k in range(2 * i-1):
            print("*" , end="")
        print()
    
    
N= int(input())
print_triangle(N)
