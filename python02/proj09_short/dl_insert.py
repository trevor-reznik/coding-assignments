"""
Author: Christian P. Byrne
File: dl_insert.py
Course: CSC120 | Summer 21

- assume head is not None
- assume node is head or another not but not None
- new_node, next and prev are both None

return poitner to the head after insertion

"""


def dl_insert_before(head, node, new_node):
    """Insert new_node before node in a doubly-linked list.
    Then return list.

    Args:
        head (obj) : Linked list head node.
        node (obj) : Linked list node.
        new_node (obj) : Linked list node.

    Returns:
        head (obj) : Linked list head node | None.


    """
    v1 = {
        "before": node.prev,
        "node": node,
        "after": node.next,
    }

    if v1["before"] is not None:
        v1["before"].next = new_node

    new_node.prev = v1["before"]
    new_node.next = v1["node"]

    node.prev = new_node

    if v1["before"] is None:
        return new_node
    else:
        return head


def dl_insert_after(head, node, new_node):
    """Insert new_node after node in a doubly-linked list.
    Then return list.

    Args:
        head (obj) : Linked list head node.
        node (obj) : Linked list node.
        new_node (obj) : Linked list node.

    Returns:
        head (obj) : Linked list head node | None.


    """
    v1 = {
        "before": node.prev,
        "node": node,
        "after": node.next,
    }

    if v1["after"] is not None:
        v1["after"].prev = new_node

    new_node.next = v1["after"]
    new_node.prev = node

    node.next = new_node
    return head
