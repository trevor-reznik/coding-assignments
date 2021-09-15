def get_elements(dic, int1):
    a = []
    for _ in dic:
        if _[:1].isupper() == True or  _[(len(dic)-1):].isupper() == True:
            a.append(dic[_])
        else:
            if dic[_] >= int1:
                a.append(dic[_])
    return a
