ret = []
for _ in open("delete.txt", "r").readlines():
    n = _.strip("|").split("|")
    ret.append(
        f"|{n[0]}  |{n[1]}  |{n[2].replace('`','')}  |"
    )

for _ in ret:
    print(_)