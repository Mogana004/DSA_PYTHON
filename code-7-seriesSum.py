
x = int(input("Enter the value of x: "))
N = int(input("Enter the number of terms (N): "))
total_sum = 0

for i in range(1, 2*N, 2):
    power = x ** i
    total_sum += power

print("The sum of the series is:", total_sum)
