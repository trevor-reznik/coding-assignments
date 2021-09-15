#! /usr/bin/python3

""" Code to test the list_to_array() function

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
nodes   = [ list_node.ListNode(2),
            list_node.ListNode(3),
            list_node.ListNode(5),
            list_node.ListNode(7),
            list_node.ListNode(11),
            list_node.ListNode(13),
            list_node.ListNode(17),
            list_node.ListNode(19)  ]
in_list = nodes[0]
nodes[0].next = nodes[1]
nodes[1].next = nodes[2]
nodes[2].next = nodes[3]
nodes[3].next = nodes[4]
nodes[4].next = nodes[5]
nodes[5].next = nodes[6]
nodes[6].next = nodes[7]

# EXPECTED OUTPUT:
#   The *nodes* that we expect as the output list.  Note that we don't need to
#   explicitly check that the contents are correct (and unchanged in each
#   node), since the list-printout will implicitly check that.  But we *do*
#   want to assert that the *nodes* are in exactly the order we expect.  If
#   they aren't (but we pass the value check), then this means that the
#   student was moving values around between nodes (or, creating new nodes).
expected_out_data = nodes



###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    print("Testing list_to_array()...")
    print()
    print(f"Input list: {in_list}")

    out_data = proj03_short_lists.list_to_array(in_list)

    print(f"Returned list: {out_data}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


