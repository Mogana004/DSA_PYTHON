numbers = input()
numbers_list = numbers.split()
l = []
for number in numbers_list :
    number = int(number)
    l = l+ [number]
print(l)
