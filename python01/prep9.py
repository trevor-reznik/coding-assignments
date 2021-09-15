n = int(input("Enter factorial to calculate:\n"))
if n == 0:
    result = 0
else:
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1

print()
print(n, "factorial =", result)
