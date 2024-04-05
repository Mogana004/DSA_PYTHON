s = input()
split = s.split()
r= []
for w in split:
    if len(w) >2:
        ch = w[2]
        r  += [ch]
char_join  = ",".join(r)
print(char_join)
        
