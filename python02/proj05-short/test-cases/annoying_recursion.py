"""Annoying Recursion Short Project

annoying_recursion.py
Christian P. Byrne
CSC120 | Summer 2021 | Short Project 5

Function Requirements:
- {x | x ∈ Z, x > 0} => ret
- {0 <= x <= 3} : output hard-coded
- {4 <= x <= 7}: recursive call args hard-coded
- no loops, default params, or other func

"""


def annoying_factorial(n):
    """Returns n!. Args: n (int), n > 0"""

    # Base - hard-coded output
    base_cases = {
        3: 6,
        2: 2,
        1: 1,
        0: 1
    }
    if n in base_cases.keys():
        return base_cases[n]

    # Base - hard-coded args recursion calls
    hard_code_cases = {
        6: (6, 5),
        5: (5, 4),
        4: (4, 3)
    }
    if n in hard_code_cases.keys():
        return (
            hard_code_cases[n][0] * annoying_factorial(
                hard_code_cases[n][1]
            )
        )

    # Core
    return n * annoying_factorial(n-1)


def annoying_fibonacci(n):
    """Returns n number in Fibonacci sequence.
    Args: n (int) : n > 0, index of returned number in Fib sequence"""

    # Base - hard-coded output
    base_cases = {
        3: 2,
        2: 1,
        1: 1,
        0: 0
    }
    # Base - hard-coded args recursion calls
    hard_code_cases = {
        6: (5, 4),
        5: (4, 3),
        4: (3, 2)
    }
    if n in base_cases.keys():
        return base_cases[n]
    if n in hard_code_cases.keys():
        return (
            annoying_fibonacci(
                hard_code_cases[n][0]
            )
            + annoying_fibonacci(
                hard_code_cases[n][1]
            )
        )

    # Core
    return annoying_fibonacci(n-1) + annoying_fibonacci(n-2)


def annoying_tree_of_tuples(n):
    """builds a nested “tree” of tuples. For n=0, simply return the value 0 (not
    in a tuple). For all higher values of n, return a tuple with three elements:
    tuple : (value returned for n-1, n, value returned for n-1).
    Args: n (int), n > 0


    """
    # Base - hard-coded output
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

    # Base - hard-coded args recursion calls
    hard_code_cases = {
        6: (5, 6),
        5: (4, 5),
        4: (3, 4)
    }
    if n in hard_code_cases.keys():
        return (
            annoying_tree_of_tuples(
                hard_code_cases[n][0]
            ),
            hard_code_cases[n][1],
            annoying_tree_of_tuples(
                hard_code_cases[n][0]
            ),
        )

    # Core
    return (
        annoying_tree_of_tuples(n-1),
        n,
        annoying_tree_of_tuples(n-1)
    )


def annoying_print_downUp(n):
    """You must first print n, then n-1, all the way down to zero.
    Print zero exactly once (not twice) and then print the numbers
    in ascending order, up to n. Args: n (int), n > 0"""
    # Base - hard-coded output
    base_cases = {
        3: "3\n2\n1\n0\n1\n2\n3",
        2: "2\n1\n0\n1\n2",
        1: "1\n0\n1",
        0: 0
    }

    # Base - hard-coded args recursion calls
    hard_code_cases = {
        6: 6,
        5: 5,
        4: 4
    }
    if n in base_cases.keys():
        print(base_cases[n])
    elif n in hard_code_cases.keys():
        print(hard_code_cases[n])
        annoying_print_downUp(hard_code_cases[n]-1)
        print(hard_code_cases[n])

    # Core
    else:
        print(n)
        annoying_print_downUp(abs(n)-1)
        print(n)
