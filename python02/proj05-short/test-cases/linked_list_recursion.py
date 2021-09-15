"""Annoying Reheadsion Short Project - Linked Lists

linked_list_reheadsion.py
Christian P. Byrne
CSC120 | Summer 2021 | Short Project 5

Function Requirements:
- {head | head ∈ ListNode, None} => head
- no loops, default params, or other func
- Linked List objects


"""


def is_plus_two(head):
    """Returns True if empty, single node, or val sep always = 2, else False.
    head (obj) linked list head node"""
    cur = head
    while cur is not None and cur.next is not None:
        if cur.next.val - cur.val != 2:
            return False
        cur = cur.next
    return True


def is_plus_two_recursive(head):
    """Returns True if empty, single node, or val sep always = 2, else False.
    head (obj) linked list head node"""
    if head is None or head.next is None:
        return True
    elif head.next.val - head.val != 2:
        return False
    return is_plus_two_recursive(head.next)
