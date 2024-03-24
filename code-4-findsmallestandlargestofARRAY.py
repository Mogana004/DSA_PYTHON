def find_min_max(arr):
    left , right = 0 , len(arr) -1 
    while left <right :
        mid= (left +right) //2
        if arr[mid] >arr[right]:
            left = mid+1 
        else:
            right = mid
    
    # smallest ele is arr[left] , the pivot 
    smallest = arr[left]
    
    #largest ele is the maximum of arr
    largest = max(arr)
    return smallest ,largest 
N= int(input())
arr= list(map(int,input().split()))


#find the smallest and largest ele
smallest , largest = find_min_max(arr)

print(smallest , end=" ")
print(largest)
