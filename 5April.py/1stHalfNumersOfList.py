numbers = input()
num = numbers.split()

length = len(num)
for each_num_index in range(length):
    num[each_num_index] = int(num[each_num_index])
if length% 2 == 0 :
    half_list_length = length//2
else:
    half_list_length = (length//2) +1 
first_half_list = num[:half_list_length]
print(first_half_list)
