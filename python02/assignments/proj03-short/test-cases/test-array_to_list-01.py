#! /usr/bin/python3

""" Code to test the array_to_list() function

    Authors: Russ Lewis   (based, very vaguely, on older code by Saumya Debray)
"""

import list_node
import proj03_short_lists





###########################################################
#              INPUT AND EXPECTED OUTPUT                  #
###########################################################
# INPUT:
in_data = [ -1, "asdf", "foo", "bar", 0, 1234 ]



###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    print("Testing array_to_list()...")
    print()
    print(f"Input data: {in_data}")

    out_list = proj03_short_lists.array_to_list(in_data)

    print(f"Returned list: {out_list}")
    print()

    print("Checking to make sure that all of the nodes in the output list are")
    print("of the proper type - that is, ListNode.")
    print()

    # check that the returned value is a list
    curr  = out_list

    while curr is not None:
        if not isinstance(curr, list_node.ListNode):
            print("ERROR: One or more nodes is not of the ListNode class.  NOTE: This can happen if you copy the ListNode class into your own file, instead of using the version inside list_node.py")
            break
        
        curr   = curr.next

    print("Output list node check complete.")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


