#! /usr/bin/python3

""" Code to test the is_plus_two() function

    Authors: Russ Lewis   (based, very vaguely, on older code by Saumya Debray)
"""

import list_node
import linked_list_recursion





# INPUT:
#   First, we build a list of nodes.
#   Then we chain them together.

vals  = [-4, -2, 0, 2, 4, 4]
nodes = [list_node.ListNode(val) for val in vals]

in_list = nodes[0]
for i in range(len(vals)-1):
    nodes[i].next = nodes[i+1]



###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    print("Testing is_plus_two()...")
    print()
    print(f"Input list: {in_list}")

    retval = linked_list_recursion.is_plus_two(in_list)

    print(f"retval: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


