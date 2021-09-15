def most_common_vehicle(file):
    d = open(file, 'r')
    ct = []
    c = ["Toyota","Ford","Chevy"]
    for _ in d:
        ct.append(int(_.replace("\n","")))
    m = max(ct)
    if ct.count(m) > 1:
        print("There's a tie!")
    else:
        print(c[ct.index(m)], "most common")
