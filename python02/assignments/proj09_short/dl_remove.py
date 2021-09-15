"""
Author: Christian P. Byrne
File: dl_remove.py
Course: CSC120 | Summer 21

Spec:
    - assume head is not None
    - assume node is head or another not but not None
    - Return poitner to the head after deletion or None
      if list is now empty


"""


def dl_remove(head, node):
    """Remove node from a doubly-linked list.
    Then return list.

    Args:
        head (obj) : Linked list head node.
        node (obj) : Linked list node.

    Returns:
        head (obj) : Linked list head node | None.


    """
    if node is head and head.next is None:
        return None
    
    v1 = {
        "before": node.prev,
        "after": node.next,
    }
    if v1["after"] is not None:
        v1["after"].prev = v1["before"]
    else:
        v1["before"].next = None

    if v1["before"] is not None:
        v1["before"].next = v1["after"]
    else:
        v1["after"].prev = None

    if node is head:
        return v1["after"]
    return head
