"""Long Project 03

Script of linked list manipulation functions. Such as: check if
val properties are sorted, return sum of val properties, splice
and partition list into sub-lists based on separators/steps.

File:
    linked_list_long.py

Author:
    Christian P. Byrne

Course:
    CSC120 Summer 2021


"""

import list_node


def is_sorted(head):
    """Indicates whether or not the passed linked list is sorted in
    ascending order.

    Args:
        head (obj) : linked list head node type object with val and next
                        properties or None object.

    Returns:
        bool : True if node's values are in ascending order or less than 2
                nodes. False if not.


    """
    sorted = True
    cur = head
    while cur is not None:
        if cur.next is not None:
            if cur.next.val < cur.val:
                sorted = False
        cur = cur.next

    return sorted


def list_sum(head):
    """Sums val properties of nodes in a linked list.

    Args:
        head (obj) : linked list head node type object with val and next
                        properties or None object. val property values
                        should be int or float type.
    Returns:
        int|float : sum of all val properties of each node. 0 if empty
                        linked list.


    """
    cur = head
    ret = 0
    while cur is not None:
        ret += cur.val
        cur = cur.next

    return ret


def partition_list(head):
    """Partitions linked list into two lists using alternating nodes
    from passed list.

    Args:
        head (obj) : linked list head node type object with val and next
                        properties or None object.

    Returns:
        tuple: (
            obj : head node of even-index nodes list,
            obj : head node of odd-index nodes list
        )


    """
    cur = head
    odd_head = head.next if head is not None else None
    while cur is not None:
        temp_next = cur.next
        if temp_next is not None:
            cur.next = cur.next.next
        cur = temp_next

    return (head, odd_head)


def accordion_3(head, start_pos):
    """Removes two out of every three nodes from a linked list object.
    Starting at start_pos and keeping every third node from there.

    Args:
        head (obj) : linked list head node type object with val and next
                        properties or None object.
        start_pos (int) : positive number indicating the first node to keep
                            out of the first three nodesi. Every third node
                            is kept after start_pos index in list.

    Returns:
        obj : head node of sliced list (node at start_pos index in passed
                list). None if start_pos is invalid index.


    """
    new_head = head
    while start_pos > 0:
        if new_head is None:
            return None
        new_head = new_head.next
        start_pos -= 1

    cur = new_head
    while cur is not None:
        if cur.next is not None and cur.next.next is not None:
            cur.next = cur.next.next.next
        else:
            cur.next = None
        cur = cur.next

    return new_head


def pair(list1, list2):
    """Takes val properties of nodes at same indexes in two lists and
    creates list with nodes whose val is (node.val, node.val) tuple
    from corresponding index in list1 and list2.

    Args:
        list1 (obj) : linked list head node type object with val and next
                        properties or None object.
        list2 (obj) : linked list head node type object with val and next
                        properties or None object.

    Returns:
        obj : head node of linked list or None:
            val (tuple) : (val, val) from corresponding index in list1 and
                            list2.truncated on basis of shorter list.


    """
    cur1 = list1
    cur2 = list2
    head = list_node.ListNode(None)
    tail = head

    while cur1 is not None and cur2 is not None:
        node = list_node.ListNode(
            (cur1.val, cur2.val)
        )
        tail.next = node
        tail = node
        cur1 = cur1.next
        cur2 = cur2.next

    return head.next
