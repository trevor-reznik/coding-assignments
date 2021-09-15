
def unzip(stream):
    # stream : Array<char | tuple<number>>
    # string.length = 1
    assert type(stream) == list
    ret = []

    for elem in stream:
        assert type(elem) in [str, tuple]

        if type(elem) == str:
            assert len(elem) > 0
            for char in elem:
                ret.append(char)

        elif type(elem) == tuple:
            assert len(elem) == 2
            assert type(elem[0]) == int and type(elem[1]) == int 
            assert elem[0] > 0 and elem[1] > 0
            start_pos = len(ret) - elem[0]
            assert start_pos >= 0
            end_pos = start_pos + elem[1]

            for _ in range(start_pos, end_pos):
                car = ret[_]
                ret.append(car)
    
    return "".join(ret)