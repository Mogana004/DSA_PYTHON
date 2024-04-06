def is_prime(n):
    if (n==1 or n==0):
        return False
    for i in range(2 , n):
        if (n%i == 0):
            return False
    return True 
    


n = int(input())
print_numbers_list = []
for i in rnage(1 , n+1):
    if ( is_prime(i)):
        prime_numbers_list.append(str(i))
prime_numbers_seperated_by_spaces = " ".join(primen_numbers_list)
print(prime_numbers_seperated_by_spaces)

# call the is_prime function
