```py
def find_kth_missing_number(arr, k):
    missing_count = 0
    for i in range(1, len(arr)):
        missing_count += arr[i] - arr[i-1] - 1
        if missing_count >= k:
            return arr[i-1] + k - (missing_count - (arr[i] - arr[i-1] - 1))
    return arr[-1] + k - missing_count

if __name__ == "__main__":
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    result = find_kth_missing_number(A, K)
    print(result)
```

## Question 
given an array A of N unique numbers and an integer K , A is sorted in increasing order , write a progra to return the kth missing number starting from the leftmost number in A .. the first line of input should contain two space seperated intehers Nand K ...and second line contains N space seperated integers of A ... the output should contain the single kth missing ele . write the program in pytgon
