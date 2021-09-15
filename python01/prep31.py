def swap(dic, set1):
    a = []
    for _ in dic:
        if _ in set1:
            a.append(_)
    for _ in a:
        b = dic[_]
        dic.update({_:_})
        dic[b] = dic[_]
        del dic[_]
