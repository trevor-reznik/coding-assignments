def get_highest_sum(list2d):
    highest = 0
    for _ in list2d:
        for x in range(len(_)-1):
            if (_[x] + _[x+1]) > highest:
                highest = (_[x] + _[x+1])
    return highest
