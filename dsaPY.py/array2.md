```py
def count_special_ladders(ladder_heights):
    special_count = 1 
    max_height  = ladder_heights[-1]
    for height in reversed(ladder_heights[::-1]):
        if height > max_height :
            special_count += 1
            max_height  = height 
    return special_count
N= int(input())
heights = list(map(int, input().split()))
result = count_special_ladders(heights)
print(result)
```
## Question 
there are N ladders positioned in a straight line . A ladder is a special lader if it is taller than all the other ladder to its right side , the right mose ladder is always a special one . given an array A of N ladders height  , write an efficient program to find the count of the special ladders . the 1 st line of input contains a single integer N and second contains N space seperated integers of A .and output should be the count of special ladders . code in python
