#! /usr/bin/python3

""" Code to test the partition_list() function

    Authors: Russ Lewis   (based, very vaguely, on older code by Saumya Debray)
"""

import list_node
import linked_list_long





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
            list_node.ListNode(19),
            list_node.ListNode(23)  ]
in_list = nodes[0]
nodes[0].next = nodes[1]
nodes[1].next = nodes[2]
nodes[2].next = nodes[3]
nodes[3].next = nodes[4]
nodes[4].next = nodes[5]
nodes[5].next = nodes[6]
nodes[6].next = nodes[7]
nodes[7].next = nodes[8]

# EXPECTED OUTPUT:
#   The *nodes* that we expect as the output list.  Note that we don't need to
#   explicitly check that the contents are correct (and unchanged in each
#   node), since the list-printout will implicitly check that.  But we *do*
#   want to assert that the *nodes* are in exactly the order we expect.  If
#   they aren't (but we pass the value check), then this means that the
#   student was moving values around between nodes (or, creating new nodes).
expected_out_list1 = nodes[ ::2]
expected_out_list2 = nodes[1::2]



###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    print("Testing partition_list()...")
    print()
    print(f"Input list: {in_list}")

    (out_list1, out_list2) = linked_list_long.partition_list(in_list)

    print(f"Returned list 1: {out_list1}")
    print(f"Returned list 2: {out_list2}")
    print()

    print("Checking to make sure that all of the nodes in the output list are")
    print("from the input list.  If you see a failure reported here, then")
    print("it's likely that you did one or more of the following:")
    print("   - Created new nodes, instead of just changing the references")
    print("   - Swapped values between nodes")
    print(" ... Checking ...")

    # check that the returned value is a list
    curr  = out_list1
    count = 0

    while curr is not None:
        if not isinstance(curr, list_node.ListNode):
            print("ERROR: One or more nodes is not of the ListNode class.  NOTE: This can happen if you copy the ListNode class into your own file, instead of using the version inside list_node.py")
            break
        
        if curr not in nodes:
            print("ERROR: One of the nodes in the list that you returned was not from the original, input list.  This means that you were creating new nodes.")
            break

        if curr not in expected_out_list1:
            print("ERROR: One of the nodes in the list that you returned was supposed to have been removed; it was in the original list, but was not supposed to be in the result.")
            break
        
        if curr is not expected_out_list1[count]:
            print("ERROR: One of the nodes in the list that you returned was from the input list, but it's not in the correct position.  Probably, this means you didn't reverse the list properly.  It's also possible that you tried to swap *values*, instead of moving the nodes around.")
            break
        
        curr   = curr.next
        count += 1

    # check that the returned value is a list
    curr  = out_list2
    count = 0

    while curr is not None:
        if not isinstance(curr, list_node.ListNode):
            print("ERROR: One or more nodes is not of the ListNode class.  NOTE: This can happen if you copy the ListNode class into your own file, instead of using the version inside list_node.py")
            break
        
        if curr not in nodes:
            print("ERROR: One of the nodes in the list that you returned was not from the original, input list.  This means that you were creating new nodes.")
            break

        if curr not in expected_out_list2:
            print("ERROR: One of the nodes in the list that you returned was supposed to have been removed; it was in the original list, but was not supposed to be in the result.")
            break
        
        if curr is not expected_out_list2[count]:
            print("ERROR: One of the nodes in the list that you returned was from the input list, but it's not in the correct position.  Probably, this means you didn't reverse the list properly.  It's also possible that you tried to swap *values*, instead of moving the nodes around.")
            break
        
        curr   = curr.next
        count += 1

    print("Output list node check complete.")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


