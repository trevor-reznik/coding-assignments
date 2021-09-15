
def shape_alpha():
    return [[10, 20], 30, 40, [50, 60]]


def shape_bravo():
    x = [123, 456]
    y = [789, 1024]

    return [
        [x, y], [y, x]
    ]


def shape_charlie(arg1):
    x = [None, None]
    y = [None, None]
    z = [None, None]
    a = [None, None]
    ret = [None, None]

    x[0] = arg1
    x[1] = arg1

    y[0] = arg1
    y[1] = arg1

    z[0] = arg1
    z[1] = arg1

    a[0] = x
    a[1] = y

    ret[0] = a
    ret[1] = z

    return ret


def shape_delta(arg1, arg2):
    x = [None]
    y = [None]

    z = [None, None]
    a = [None, None]
    b = [None]


    ret = [None, None, None, None]

    x[0] = arg2
    y[0] = arg1

    z[0] = arg1
    z[1] = x

    a[0] = z
    a[1] = y

    ret[0] = arg1
    ret[1] = arg2
    ret[2] = a
    b[0] = 17
    ret[3] = b

    return ret


def shape_echo(arg1, arg2, arg3):
    x = [None, None]
    y = [None, None]
    ret = [None, None]

    x[0] = arg3
    x[1] = ret

    y[0] = arg2
    y[1] = x

    ret[0] = arg1
    ret[1] = y

    return ret 