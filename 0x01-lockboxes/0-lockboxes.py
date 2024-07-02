#!/usr/bin/python3
"""
A method to determines if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    The working script
    """
    x = len(boxes)
    item = [False] * x
    item[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for each in boxes[box]:
            if each >= 0 and each < x and not item[each]:
                item[each] = True
                stack.append(each)
    return all(item)
