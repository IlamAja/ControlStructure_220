def print_pattern(n):
    for i in range(1, n+1):
        print((str(i) + " ") * i)  


n = int(input("Enter the value of n: "))


print_pattern(n)
