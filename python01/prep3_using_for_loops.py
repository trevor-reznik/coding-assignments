width = int(input("Rectangle width:\n"))
height = int(input("Rectangle height:\n"))

print()
for _ in range(height):
    for _ in range(width):
        print("#", end="")
    print()