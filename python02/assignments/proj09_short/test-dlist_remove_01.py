#!/usr/bin/env python3

""" Code to test dl_remove() """


import dlist_node
import utils

import dl_remove



# ------- CONFIG VALUES ------
# (Change these to alter what the testcase does)

values = ["abc",123,"foo","bar","baz",1024,-1,"qwerty"]
rem_pos = 0


# ------- DERIVED VALUES ------
# (These are inputs, but they are calculated from the config variables above)

nodes  = [dlist_node.DListNode(v) for v in values]
for i in range(len(values)-1):
    nodes[i  ].next = nodes[i+1]
    nodes[i+1].prev = nodes[i]
head = nodes[0]

# sanity check that I've set the list up properly.
assert utils.dlist_is_consistent(head)

# this is the node which we plan to remove.
rem_node = nodes[rem_pos]



# ------- TESTCASE BODY --------
print("Testing the dl_remove() function")
print()

print(f"Starting list:   {utils.dlist_to_str(head)}")
print(f"Remove position: {rem_pos}")
print()

print("Calling dl_remove()...")
head = dl_remove.dl_remove(head, rem_node)
print()

print("Confirming that the new list follows the rules of a doubly-linked-list...")
if utils.dlist_is_consistent(head):
    print("  Results: OK")
else:
    print("  Results: FAIL    (see the previous messages for an explanation)")

print(f"List after remove: {utils.dlist_to_str(head)}")
print()

print("TESTCASE COMPLETED")


