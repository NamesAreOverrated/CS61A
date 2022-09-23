email = 'example_key'


def copycat(lst1, lst2):
    """
    Write a function `copycat` that takes in two lists.
        `lst1` is a list of strings
        `lst2` is a list of integers

    It returns a new list where every element from `lst1` is copied the
    number of times as the corresponding element in `lst2`. If the number
    of times to be copied is negative (-k), then it removes the previous
    k elements added.

    Note 1: `lst1` and `lst2` do not have to be the same length, simply ignore
    any extra elements in the longer list.

    Note 2: you can assume that you will never be asked to delete more
    elements than exist


    >>> copycat(['a', 'b', 'c'], [1, 2, 3])
    ['a', 'b', 'b', 'c', 'c', 'c']
    >>> copycat(['a', 'b', 'c'], [3])
    ['a', 'a', 'a']
    >>> copycat(['a', 'b', 'c'], [0, 2, 0])
    ['b', 'b']
    >>> copycat([], [1,2,3])
    []
    >>> copycat(['a', 'b', 'c'], [1, -1, 3])
    ['c', 'c', 'c']
    """
    def copycat_helper(lst=[], index=0, count=0):
        if index >= len(lst1) or index >= len(lst2):
            return lst
        if count == 0:
            return copycat_helper(lst, index+1, lst2[index+1]
                                  if len(lst2) > index+1 else 0)
        if lst2[index] > 0:
            lst.append(lst1[index])
            return copycat_helper(lst, index, count-1)
        else:
            lst.pop(0)
            return copycat_helper(lst, index, count+1)
    return copycat_helper(count=lst2[0]
                          if len(lst2) > 0 else 0)

# ORIGINAL SKELETON FOLLOWS

# def copycat(lst1, lst2):
#     """
#     Write a function `copycat` that takes in two lists.
#         `lst1` is a list of strings
#         `lst2` is a list of integers

#     It returns a new list where every element from `lst1` is copied the
#     number of times as the corresponding element in `lst2`. If the number
#     of times to be copied is negative (-k), then it removes the previous
#     k elements added.

#     Note 1: `lst1` and `lst2` do not have to be the same length, simply ignore
#     any extra elements in the longer list.

#     Note 2: you can assume that you will never be asked to delete more
#     elements than exist


#     >>> copycat(['a', 'b', 'c'], [1, 2, 3])
#     ['a', 'b', 'b', 'c', 'c', 'c']
#     >>> copycat(['a', 'b', 'c'], [3])
#     ['a', 'a', 'a']
#     >>> copycat(['a', 'b', 'c'], [0, 2, 0])
#     ['b', 'b']
#     >>> copycat([], [1,2,3])
#     []
#     >>> copycat(['a', 'b', 'c'], [1, -1, 3])
#     ['c', 'c', 'c']
#     """
#     def copycat_helper(______, ______, ______):
#         if ______:
#             return ______
#         if ______:
#             ______ = ______
#         else:
#             ______ = ______[:______]
#         return ______
#     return ______
