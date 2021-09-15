
data=[None, None, None]

for i in range(2):
    data[i] = [3*i, 2*i, 1*i]
    print(data[0][0] is data[0][1])
data[2] = data


print(data)

print(
    id(data)
)

print(
    id(data[2])
)
x = 1
data = x
print(
    id(data)
)