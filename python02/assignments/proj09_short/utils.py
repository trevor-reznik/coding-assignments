#!/usr/bin/env python3

""" Helpful utilities, used by various testcases in testing dlist_node. """



# NOTE: It's not necessary to import the dlist_node file, since we don't actually
#       create any *new* objects in these functions.



def dlist_is_consistent(head):
    """ Returns True if the list appears to be valid (that is, has all the
        proper next/prev pointers, and the head is actually the head of the list)

        Note that head is a pointer to what we believe is the head of the list
        (might be none).
    """

    if head is None:
        # trivially OK!
        return True

    if head.prev is not None:
        print(f"ERROR: The node that we think is the head of the list (the node containing {head.val}) has a non-None prev pointer.")
        return False

    cur = head
    while cur is not None:
        if cur.prev is not None:
            if cur.prev.next is not cur:
                print("ERROR: next/prev mismatch detected.")
                print(f"        current   node: id={id(cur)}   value: {cur.val}")
                print(f"        prev      node: id={id(cur.prev)}   value: {cur.prev.val}")
                print(f"        prev.next node: id={id(cur.prev.next)}   --- value not printed ---")
                return False
        else:
            if cur is not head:
                print(f"ERROR: The list node containing {cur.val} is not the head, but its prev link is None.")
                return False

        cur = cur.next

    return True



def dlist_to_str(dllist):
    """ convert a doubly-linked list to a string """
    if dllist is None:
        return "None"
    else:
        cur = dllist        
        vals, objs = [], []
        while cur is not None:
            cur_str = str(cur.val)
            if cur in objs:
                vals.append(cur_str+" <=> ... (to infinity and beyond)")
                break
            else:
                vals.append(cur_str)
                objs.append(cur)
            cur = cur.next

        return " <=> ".join(vals)


