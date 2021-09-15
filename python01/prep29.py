def sum_nums(li2):
    a=0
    for _ in li2:
        for x in _:
            if x < 10:
               a+=x
    return a
