```py
rows = int(input())
for each_number in range( 1, rows+1):
    spaces = " " * ( rows- each_number)
    stars= "*" * (each_number)
    print(spaces + stars)

```
