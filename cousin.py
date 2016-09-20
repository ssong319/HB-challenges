"""Find 'cousin' nodes -- those nodes at the same level as a node.

Consider the tree::

            a
        ---------
       /    |    \
      b     c     d
     /-\   /-\   /-\
    e  f  g  h  i  j
        \     \
        k     l

Nodes `k` and `l` are at same level ("cousins", a we'll call them, but removed
by several levels). Similarly `e`, `f`, `g`, `h`, `i`, and `j` are cousins, as are
`b`, `c`, and `d`.

Let's create this tree::

    >>> a = Node("a")

    >>> b = Node("b")
    >>> c = Node("c")
    >>> d = Node("d")
    >>> b.set_parent(a)
    >>> c.set_parent(a)
    >>> d.set_parent(a)

    >>> e = Node("e")
    >>> f = Node("f")
    >>> g = Node("g")
    >>> h = Node("h")
    >>> i = Node("i")
    >>> j = Node("j")
    >>> e.set_parent(b)
    >>> f.set_parent(b)
    >>> g.set_parent(c)
    >>> h.set_parent(c)
    >>> i.set_parent(d)
    >>> j.set_parent(d)

    >>> k = Node("k")
    >>> l = Node("l")
    >>> k.set_parent(f)
    >>> l.set_parent(h)

Let's find the cousins for b::

    >>> b.cousins() == {c, d}
    True

    >>> c.cousins() == {b, d}
    True

    >>> e.cousins() == {f, g, h, i, j}
    True

    >>> k.cousins() == {l}
    True

The root node has no cousins::

    >>> a.cousins() == set()
    True
"""


class Node(object):
    """Doubly-linked node in a tree.

        >>> na = Node("na")
        >>> nb1 = Node("nb1")
        >>> nb2 = Node("nb2")

        >>> nb1.set_parent(na)
        >>> nb2.set_parent(na)

        >>> na.children
        [<Node nb1>, <Node nb2>]

        >>> nb1.parent
        <Node na>
    """

    parent = None

    def __init__(self, data):
        self.children = []
        self.data = data

    def __repr__(self):
        return "<Node %s>" % self.data

    def set_parent(self, parent):
        """Set parent of this node.

        Also sets the children of the parent to include this node.
        """

        self.parent = parent
        parent.children.append(self)

    def cousins(self):
        """Find nodes on the same level as this node."""

        #find depth of current node. Counting up
        depth = 0
        higher = self

        while higher.parent is not None:
            depth += 1
            higher = higher.parent

        #handle root node case
        if depth == 0:
            return set()

        #depth is now where it should be, higher is now the root of whole tree
        #when you add children is when you increment place til you reach depth
        place = 0

        visit = [higher]

        #keep taking off the elements in visit and add its children til we're at the correct place
        while place < depth:
            children = []
            place += 1
            while visit:
                x = visit.pop()
                children.extend(x.children)
            visit.extend(children)

        visit.remove(self)

        cousin_set = set(visit)

        return cousin_set




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB! ***\n"
