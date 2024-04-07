s = input().split()

output=""
for char in s:
    
    first_word = char[0]
    
    output += first_word
print(".".join(output))
