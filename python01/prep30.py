def longest_string(dicList):
    longest = ""
    for dic in dicList:
        for _ in dic.values():
            if len(_) > len(longest):
                longest = _           
    return longest
