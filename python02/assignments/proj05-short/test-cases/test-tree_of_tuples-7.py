#! /usr/bin/python3

""" Code to test the annoying_tree_of_tuples() function

    Author: Russ Lewis
"""

import annoying_recursion





###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    val = 7

    print("Testing annoying_tree_of_tuples()...")
    print()
    print(f"Input val: {val}")

    retval = annoying_recursion.annoying_tree_of_tuples(val)

    print(f"Returned val: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


