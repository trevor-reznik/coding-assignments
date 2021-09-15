def get_common_movies(setList):
    a = set()
    for _ in setList:
        for x in _:
            b = 2
            for z in setList:
                if x not in z:
                    b = 1
            if b == 2 and x not in a:
                a.add(x)
    return a
