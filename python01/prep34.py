def get_highest_neighbor(list2d, i1, i2):
    ct = []
    top = i1 -1
    bottom = i1 + 1
    right = i2 + 1
    left = i2 - 1
    if i1 == 0:
        if i2 == 0:
            rightN = list2d[i1][right]
            botN = list2d[bottom][i2]
            ct.append(rightN);ct.append(botN)
        if i2 == len(list2d[i1]):
            leftN = list2d[i1][left]
            botN = list2d[bottom][i2]
            ct.append(leftN);ct.append(botN)
        else:
            leftN = list2d[i1][left]
            rightN = list2d[i1][right]
            botN = list2d[bottom][i2]
            ct.append(leftN);ct.append(rightN);ct.append(botN)
    if i1 == len(list2d)-1:
        if i2 == 0:
            topN = list2d[top][i2]
            rightN = list2d[i1][right]
            ct.append(topN);ct.append(rightN)
        if i2 == len(list2d[i1]):
            topN = list2d[top][i2]
            leftN = list2d[i1][left]
            ct.append(topN);ct.append(leftN)
        else:
            topN = list2d[top][i2]
            leftN = list2d[i1][left]
            rightN = list2d[i1][right]
            ct.append(topN);ct.append(leftN);ct.append(rightN)
    else:
        if i2 == 0:
            topN = list2d[top][i2]
            rightN = list2d[i1][right]
            botN = list2d[bottom][i2]
            ct.append(topN);ct.append(rightN);ct.append(botN)
        if i2 == len(list2d[i1]):
            topN = list2d[top][i2]
            leftN = list2d[i1][left]
            botN = list2d[bottom][i2]
            ct.append(topN);ct.append(leftN);ct.append(botN)
        else:
            topN = list2d[top][i2]
            leftN = list2d[i1][left]
            rightN = list2d[i1][right]
            botN = list2d[bottom][i2]
            ct.append(topN);ct.append(leftN);ct.append(rightN);ct.append(botN)
    return max(ct)
