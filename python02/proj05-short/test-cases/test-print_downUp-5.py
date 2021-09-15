#! /usr/bin/python3

""" Code to test the annoying_print_downUp() function

    Author: Russ Lewis
"""

import annoying_recursion





###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    val = 5

    print("Testing annoying_print_downUp()...")
    print()
    print(f"Input val: {val}")

    annoying_recursion.annoying_print_downUp(val)

    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


