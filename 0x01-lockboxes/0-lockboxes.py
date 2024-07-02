#!/usr/bin/python3
"""
A method to determines if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    The working script
    """


if not isinstance(boxes, list) or len(boxes) == 0:
    return False

    n = len(boxes)
    opened = [False] * n
    opened[0] = True  # The first box is always open
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
