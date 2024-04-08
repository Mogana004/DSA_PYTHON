n= int(input())
array = list(map(int , input().split()))
k = int(input())

k = k % n 
rotated_arr = array[-k:] + array[ :-k]
rotated_arr_str = " ".join(map(str, rotated_arr))
print(rotated_arr_str)
