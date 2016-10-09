"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""
    stack = []
    rev_s = s[::-1]
    for ele in rev_s:
        if ele.isdigit():
            stack.append(int(ele))
        elif ele == "-":
            calc = stack[-1] - stack[0]
            stack = [calc]
        elif ele == "+":
            calc = stack[-1] + stack[0]
            stack = [calc]
        elif ele == "*":
            calc = stack[-1] * stack[0]
            stack = [calc]
        elif ele == "/":
            calc = stack[-1] / stack[0]
            stack = [calc]
    return stack[0]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n"
