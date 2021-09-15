#! /usr/bin/python3

""" Code to test the list_length() function

    Authors: Russ Lewis   (based, very vaguely, on older code by Saumya Debray)
"""

import list_node
import proj03_short_lists





###########################################################
#              INPUT AND EXPECTED OUTPUT                  #
###########################################################
# INPUT:
#   First, we build a list of nodes.
#   Then we chain them together.
nodes   = [ list_node.ListNode("abc"),
            list_node.ListNode("def"),
            list_node.ListNode("ghi") ]

in_list = nodes[0]
nodes[0].next = nodes[1]
nodes[1].next = nodes[2]

# EXPECTED OUTPUT:
#   The *nodes* that we expect as the output list.  Note that we don't need to
#   explicitly check that the contents are correct (and unchanged in each
#   node), since the list-printout will implicitly check that.  But we *do*
#   want to assert that the *nodes* are in exactly the order we expect.  If
#   they aren't (but we pass the value check), then this means that the
#   student was moving values around between nodes (or, creating new nodes).
expected_out_list = nodes[1::2]



###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    print("Testing list_length()...")
    print()
    print(f"Input list: {in_list}")

    out_val = proj03_short_lists.list_length(in_list)

    print(f"Returned val: {out_val}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


