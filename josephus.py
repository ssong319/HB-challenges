"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31

As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""

class Node(object):
    """Doubly-linked node."""

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return "<Node prev=%s data=%s next=%s>" % (
            self.prev.data, self.data, self.next.data)


#my sol (also see HB sol)

def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""
    #populate list with people
    list_of_people = []
    for k in range(1, num_people + 1):
        list_of_people.append(k)

    start_node = Node(list_of_people[0])
    before_node = start_node

    #create a circular, doubly linked list
    for i in range(1, len(list_of_people)):
        new_node = Node(list_of_people[i], prev=before_node, next=None)
        before_node.next = new_node
        before_node = before_node.next

        if i == len(list_of_people) - 1:
            new_node.next = start_node
            start_node.prev = new_node

    current = start_node
    #traverse the linked list, removing every kill_everyth node
    while True:
        for i in range(1, kill_every + 1):
            if i == kill_every:
                previous_node = current.prev
                after_node = current.next
                #when down to two nodes, the survivor is the other node
                if previous_node == after_node:
                    return previous_node.data

                previous_node.next = after_node
                after_node.prev = previous_node
            current = current.next




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
