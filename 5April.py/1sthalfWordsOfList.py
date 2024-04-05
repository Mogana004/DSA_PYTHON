sentence = input()
words = sentence.split()
length = len(words)

if length %2 == 0 :
    half = length//2
else:
    half = (length//2) +1 
new_list = words[:half]
print(new_list)
