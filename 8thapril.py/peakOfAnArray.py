N= int(input())
array = list(map(int , input().split()))
peak_element = 0 
for i in range(1 , len(array)):
    if array[i] > array[peak_element]:
        peak_element = i 
print(peak_element)
    
