def every_other(string):
    string = string.split(" ")
    a = ""
    for _ in range(len(string)):
        if _ % 2 == 0:
            a += string[_] + " "
    return a
