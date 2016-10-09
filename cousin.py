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

    >>> k.find_common_ancestor(k, l) == 'a'
    True

    >>> k.find_common_ancestor(l, g) == 'c'
    True

    >>> k.find_common_ancestor(f, g) == 'a'
    True

    >>> k.find_common_ancestor(i, j) == 'd'
    True

    >>> k.find_common_ancestor(i, i) == 'i'
    True

    >>> k.find_common_ancestor(c, l) == 'c'
    True

    >>> k.find_common_ancestor(a, a) == 'a'
    True

    >>> k.find_common_ancestor(a, c) == 'a'
    True

    >>> find_path(a, k) == [a, b, f, k]
    True

    >>> find_path(a, l) == [a, c, h, l]
    True

    >>> find_path(a, d) == [a, d]
    True

    >>> find_path(a, a) == [a]
    True

    >>> find_path(a, f) == [a, b, f]
    True

    >>> find_path(a, g) == [a, c, g]
    True

    >>> a.find_common_ancestor_wo_par(a, k, l) == a
    True

    >>> a.find_common_ancestor_wo_par(a, l, g) == c
    True

    >>> a.find_common_ancestor_wo_par(a, f, g) == a
    True

    >>> a.find_common_ancestor_wo_par(a, i, j) == d
    True

    >>> a.find_common_ancestor_wo_par(a, i, i) == i
    True

    >>> a.find_common_ancestor_wo_par(a, a, a) == a
    True

    >>> a.find_common_ancestor_wo_par(a, a, c) == a
    True

    >>> a.find_common_ancestor_wo_par(a, c, l) == c
    True

    >>> a.find_common_ancestor_wo_par(a, e, j) == a
    True
"""


#find respective paths of nodes in a tree given root node, DFS
def find_path(root, node1, path=[]):

    path = path + [root]

    current = root

    if not current.children and current.data != node1.data:
        return None

    if current.data == node1.data:
        return path

    for child in current.children:
        newpaths = find_path(child, node1, path)

        if newpaths:
            return newpaths


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


    def find_common_ancestor(self, node1, node2):
        """
        Given two nodes, find the least common ancestor. The ancestor can be the node itself.
        """
        #create empty set to keep track of the nodes' respective parents, initialize it with the node itself

        node1_par = set([node1])
        node2_par = set([node2])

        current1 = node1.parent
        current2 = node2.parent

        while node1_par & node2_par == set():
            node1_par.add(current1)
            node2_par.add(current2)

            if current1:
                current1 = current1.parent
            if current2:
                current2 = current2.parent

        return (node1_par & node2_par).pop().data


    def find_common_ancestor_wo_par(self, root, node1, node2):
        path1 = find_path(root, node1)
        path2 = find_path(root, node2)

        path1.reverse()
        path2.reverse()

        for p in path1:
            if p in path2:
                return p






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB! ***\n"
