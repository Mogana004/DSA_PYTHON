nums = str(input()).split(" ")
product = 1 
s= ""
for i in range(0 , len(nums)):
    product = product * int(nums[i])
    s= s+ nums[i] + " X "
print(product)
