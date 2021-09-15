pairs = {}
for line in open(
    input("File to scan: ").strip(),
    "r"
    ).readlines():

    if line.strip() and not line.strip().startswith("#"):
        unpacked = line.split()
        if unpacked[0] in pairs.keys():
             pairs[unpacked[0]] += int(unpacked[1])
        else:
            pairs[unpacked[0]] = int(unpacked[1])

print("STEP 1: THE ORIGINAL DICTIONARY")
for word, num in sorted(pairs.items()):
    print("Key:", word, "Value:", num)

print(
    "\nSTEP 2: A LIST OF VALUE->KEY TUPLES",
    [(num, word) for word, num in sorted(pairs.items())],
    "\nSTEP 3: AFTER SORTING",
    sorted(zip(pairs.values(),pairs.keys())),
    "\nSTEP 4: THE ACTUAL OUTPUT",
    sep="\n"
)

for num, word in sorted(zip(pairs.values(),pairs.keys())):
    print(word, num)