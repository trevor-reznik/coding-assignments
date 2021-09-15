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
nodes = [ ]

in_list = None

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


