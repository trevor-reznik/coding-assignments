x = [10, None]
tail = x
# DRAW HERE
for i in range(4):
    print(i)
    tail[1] = [ i*10+20, None ]
    tail = tail[1]

    if i == 0:
        print(tail is x[1])
    
    if i == 1:
        print(tail is x[1][1])
    
    if i == 2:
        print(tail is x[1][1][1])
    
    if i == 3:
        print(tail is x[1][1][1][1])
    
    print("tail:")
    print(tail)
    # DRAW HERE
    print(x)
    print()

print("\n\n\n\n")    
print(x)


