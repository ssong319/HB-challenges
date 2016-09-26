"""Given linked list, reverse the nodes in this linked list in place.

For example:

    >>> ll = LinkedList(Node(1, Node(2, Node(3))))
    >>> reverse_linked_list_in_place(ll)
    >>> ll.as_string()
    '321'

"""


class LinkedList(object):
    """Linked list."""

    def __init__(self, head=None):
        self.head = head

    def as_string(self):
        """Represent data for this list as a string.

        >>> LinkedList(Node(3)).as_string()
        '3'

        >>> LinkedList(Node(3, Node(2, Node(1)))).as_string()
        '321'
        """

        out = []
        n = self.head

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next



def reverse_linked_list_in_place(lst):
    """Given linked list, reverse the nodes in this linked list in place."""
    current_head = lst.head
    prev = None

    while current_head is not None:
        start = current_head.next
        current_head.next = prev
        prev = current_head
        current_head = start

    lst.head = prev


#HB sol - recursive solution
def reverse_linked_list_in_place(lst):
    """Given linked list, recursively reverse
    the nodes in this linked list in place."""

    # We use a helper function that takes
    # as argument the first node of a linked list

    lst.head = _reverse(lst.head)

def _reverse(node):
    """Helper function that does the recursion."""

    # base case is single node
    if node.next is None:
        return node

    # recurse to get the reversed smaller list
    reversed_ = _reverse(node.next)

    # find last node of smaller list
    current = reversed_
    while current.next is not None:
        current = current.next

    # add our node to end
    current.next = node
    node.next = None

    return reversed_










if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"
