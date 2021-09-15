#! /usr/bin/python3

""" Code to test the annoying_factorial() function

    Author: Russ Lewis
"""

import annoying_recursion





###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    val = 0

    print("Testing annoying_factorial()...")
    print()
    print(f"Input val: {val}")

    retval = annoying_recursion.annoying_factorial(val)

    print(f"Returned val: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


