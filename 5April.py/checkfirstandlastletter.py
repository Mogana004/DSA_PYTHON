line = input()
u = line.upper()
word = u.split()

for w in word:
    f = w[0]
    l = w[-1] 
    if f== l :
        print("True")
    else:
        print("False")
