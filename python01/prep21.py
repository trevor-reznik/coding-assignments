def get_supply_count():
    z = open('supplies.txt', 'r')
    a = 0
    for _ in z:
        n = _.split(" ")
        n[1] = n[1].replace("\n","")
        if n[1] != "":
            a += int(n[1])
    b = open("total.txt","w")
    b.write(str(a))
