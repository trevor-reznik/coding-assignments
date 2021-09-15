

def annoying_x(int_arg):
    if int_arg in [0, 1, 2, 3]:
        return int_arg

# 4-7 hard-coded
#


def annoying_factorial(n):
    base_cases = {
        3: 6,
        2: 2,
        1: 1,
        0: 1
    }
    if n in base_cases.keys():
        return base_cases[n]
    if n == 6:
        return 6 * annoying_factorial(5)
    if n == 5:
        return 5 * annoying_factorial(4)
    if n == 4:
        return 4 * annoying_factorial(3)
    return n * annoying_factorial(n-1)


def annoying_fibonacci(n):
    base_cases = {
        3: 2,
        2: 1,
        1: 1,
        0: 0
    }
    if n in base_cases.keys():
        return base_cases[n]
    if n == 6:
        return annoying_fibonacci(5) + annoying_fibonacci(4)
    if n == 5:
        return annoying_fibonacci(4) + annoying_fibonacci(3)
    if n == 4:
        return annoying_fibonacci(3) + annoying_fibonacci(2)
    return annoying_fibonacci(n-1) + annoying_fibonacci(n-2)


def annoying_tree_of_tuples(n):
    base_cases = {
        3: (
            (
                (0, 1, 0),
                2,
                (0, 1, 0)
            ),
            3,
            (
                (0, 1, 0),
                2,
                (0, 1, 0)
            )
        ),
        2: (
            (0, 1, 0),
            2,
            (0, 1, 0)
        ),
        1: (0, 1, 0),
        0: 0
    }
    if n in base_cases.keys():
        return base_cases[n]
    if n == 6:
        return (
            annoying_tree_of_tuples(5),
            6,
            annoying_tree_of_tuples(5)
        )
    if n == 5:
        return (
            annoying_tree_of_tuples(4),
            5,
            annoying_tree_of_tuples(4)
        )
    if n == 4:
        return (
            annoying_tree_of_tuples(3),
            4,
            annoying_tree_of_tuples(3)
        )
    return (
        annoying_tree_of_tuples(n-1),
        n,
        annoying_tree_of_tuples(n-1)
    )


def annoying_print_downUp(n):
    if n % 1 == 0 and type(n) == float:
        return 0
    
    ceiling = (n // 1) + 1
    iterations = ( float(ceiling) - n ) / .10
    carry = (iterations*10) * -.20
    p = abs(carry + n)
    print(p)
    # carry = distance from floor roudned up
    # abs value print
    return annoying_print_downUp(n-.10)

def annoying_print_downUp(n):

    base = str(float(n)).split(".")[0]
    decimal_places = str(float(n)).split(".")[1]

    cur_place =  len(decimal_places) + 1
    modifier = 10**cur_place
    
    previous = float(
        str(n)[-1]
    )

    if len(decimal_places) >= int(base):
        after = previous + 1.0
    else:
        after = previous - 1.0
    if len(str(n))< 2:
        print(base)
    
    print(int(after)-1)
    
    after = after / modifier
    new = float(n) + after
    
    if len(decimal_places) >= int(base)*2-2:
        print(base)
        return 0
    
    return annoying_print_downUp(new)

def annoying_print_downUp(n):
    print(n)
    if n == 0:
        return n+2
    base_cases = {
        3: 2,
        2: 1,
        1: 1,
        0: 0
    }
    if n in base_cases.keys():
        return base_cases[n]
    if n == 6:
        return annoying_fibonacci(5) + annoying_fibonacci(4)
    if n == 5:
        return annoying_fibonacci(4) + annoying_fibonacci(3)
    if n == 4:
        return annoying_fibonacci(3) + annoying_fibonacci(2)
    return annoying_fibonacci(n-1) + annoying_fibonacci(n-2)

def annoying_print_downUp(n):
    print(n)
    if n == 0:
        
    return annoying_print_downUp(n - (n-1))
    

annoying_print_downUp(4)