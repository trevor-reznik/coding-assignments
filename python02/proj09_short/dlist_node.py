
class DListNode:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None


    def __str__(self):
        # go back, and find the start of the list
        cur = self
        while cur.prev is not None:
            cur = cur.prev

        # iterate through the list, starting from the head, using a special
        # mark to designate the 'self' pointer that was passed.
        retval_list = []
        while cur is not None:
            if cur is self:
                retval_list.append("(self: {})".format(cur.val))
            else:
                retval_list.append(cur.val)
            cur = cur.next

        return " -> ".join(retval_list)


