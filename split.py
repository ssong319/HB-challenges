"""Split astring by splitter and return list of splits.

This should work like that built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implemented that.

"""


def split(astring, splitter):
    """Split astring by splitter and return list of splits."""
    lst = []
    start_pos = 0
    sl = len(splitter)

    for i in range(len(astring)):
        if astring[i: i + sl] == splitter:
            lst.append(astring[start_pos:i])
            start_pos += i - start_pos + sl

    lst.append(astring[start_pos:])
    return lst


#HB solution using find method
def split(astring, splitter):
    """Split astring by splitter and return list of splits."""
    out = []
    index = 0

    while index <= len(astring):

        curr_index = index
        index = astring.find(splitter, index)

        if index != -1:
            out.append(astring[curr_index:index])
            index += len(splitter)

        else:
            # couldn't find any more instances of splitter in astring
            out.append(astring[curr_index:])
            break

    return out



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. FINE SPLITTING!\n"
