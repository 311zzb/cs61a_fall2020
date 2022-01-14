def find_paths(t, entry): # CS61a fa20 Disc08
    """
    >>> from tree import *
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    # t = Tree(6, [Tree(5), Tree(5)]), entry = 5
    paths = []
    if t.label == entry: # if 6 == 5
        paths.append([entry])
    for b in t.branches: # b = Tree(5), b = Tree(5)
        if find_paths(b, entry):
            # paths += [[6] + [5]], paths += [[6] + [5]]
            paths += [[t.label] + item for item in find_paths(b, entry)]
    return paths # paths = [[6, 5], [6, 5]]


def close(n, smallest=10, d=10): # CS61a su20 mt practice q3
    """ A sequence is near increasing if each element but the last two is smaller
    than all elements following its subsequent element. That is, element i must
    be smaller than elements i + 2, i + 3, i + 4.
    Implement close, which takes a non-negative integer n and returns the largest
    near incresing sequence of digits within n as an integer. The arguments smallest
    and d are part of the implementation; you must determine their purpose. The
    only values you may use are integers and booleans (no lists, strings, etc.).
    Return the longest sequence of near-increasing digits in n.

    >>> close(123)
    123
    >>> close(153)
    153
    >>> close(1523)
    153
    >>> close(15123)
    1123
    >>> close(11111111)
    11
    >>> close(985357)
    557
    >>> close(14735476)
    143576
    >>> close(812348567)
    1234567
    >>> close(45671)
    4567
    """
    # Plan:
    # 1) Forget about n % 10 and just find close(n // 10)
    # OR
    # 2) Use          n % 10 and make sure everything before it forms a
    # "near-increasing" sequence
    # Return whichever is longer(i.e. bigger) among (1) and (2).
    if n == 0:
        return 0
    no = close(n // 10, smallest, d)
    if smallest > n % 10:
        yes = close(n // 10, min(smallest, d), n % 10) * 10 + n % 10
        return max(yes, no)
    return no


def num_trees(n): # CS61a fa20 lab09 Q4
    """How many full binary trees have exactly n leaves? E.g.,

    1   2        3       3    ...
    *   *        *       *
       / \      / \     / \
      *   *    *   *   *   *
              / \         / \
             *   *       *   *

    >>> num_trees(1)
    1
    >>> num_trees(2)
    1
    >>> num_trees(3)
    2
    >>> num_trees(8)
    429
    """
    # Number of leaves in the left branch + number of leaved in the right branch = n
    # num_trees_on_left * num_trees_on_right for num_leaved_on_left in range(1, n)
    if n == 1:
        return 1
    return sum([num_trees(i) * num_trees(n-i) for i in range(1,n)])


def num_splits(s, d): # CS61a fa20 lab14 Q4
    """Return the number of ways in which s can be partitioned into two
    sublists that have sums within d of each other.

    >>> num_splits([1, 5, 4], 0)  # splits to [1, 4] and [5]
    1
    >>> num_splits([6, 1, 3], 1)  # no split possible
    0
    >>> num_splits([-2, 1, 3], 2) # [-2, 3], [1] and [-2, 1, 3], []
    2
    >>> num_splits([1, 4, 6, 8, 2, 9, 5], 3)
    12
    """
    def helper(s, n):
        # S is a list, N is the running difference
        if len(s) == 0:
            return 1 if abs(n) <= d else 0
        else:
            #                    Use s[0]                  Drop s[0]
            return helper(s[1:], n + s[0]) + helper(s[1:], n - s[0])
    return helper(s, 0) // 2
