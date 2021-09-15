feet = int(input("Number of feet:\n"))

inches = feet * 12

meters = round((feet * float(0.3048)), 3)

rods = round((feet / float(16.5)), 1)

print(" \nInches:", inches)
print("Meter:", meters)
print("Rods:", rods)