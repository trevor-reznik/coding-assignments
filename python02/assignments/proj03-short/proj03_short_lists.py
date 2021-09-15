"""Short Project 3 - Linked List Manipulation

Script of functions to split linked lists, get their length, 
conver them to arrays, or convert arrays to linked lists.
https://lecturer-russ.appspot.com/classes/cs120/summer21/projects/proj03-short.pdf

Author: Christian P. Byrne
Course: CSC337 Summer 2021
"""

import list_node


def list_to_array(head):
    """Convert linked list object to an array and return the array.

    Args:
        head (obj) : linked list head node.
    
    Returns:
        list : the val properties of each node in the head list.
    
    
    """
    cur = head
    ret = []
    while cur is not None:
        ret.append(
            cur.val
        )
        cur = cur.next
    
    return ret


def array_to_list(data):
    """Convert array to linked list object and return array.

    Args:
        data (list) : array of any type elements.

    Returns:
        obj : linked list object


    """
    nodes = []
    for e in data:
        nodes.append(
            list_node.ListNode(e)
        )

    for index, node in enumerate(nodes):
        if index < len(nodes) - 1:
            node.next = nodes[index + 1]
        else:
            node.next = None
        
    return nodes[0] if nodes else None

 
def list_length(head):
    """Get length of linked list object.

    Args:
        head (obj) : head node of a linked list.

    Returns:
        int : length of linked list


    """
    cur = head
    ct = 0
    while cur is not None:
        ct += 1
        cur = cur.next

    return ct


def split_list(old_head):
    """Split linked list in half and returns head nodes of both 
    sub-lists.
    
    Args:
        old_head (obj) : head node of linked list obj.

    Returns:
        tuple: (head node 1, head node 2).


    """
    ct = list_length(old_head)
    halfway = ct//2 + 1 if ct % 2 else ct // 2

    cur = old_head
    index = 0
    while index != halfway - 1:
        index += 1
        cur = cur.next

    new_head = cur.next
    cur.next = None
    return (old_head, new_head)