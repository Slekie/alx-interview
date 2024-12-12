#!/usr/bin/python3
""" method to open locked boxes """


def canUnlockAll(boxes):
    """ ... """
    unlocked = set([0])
    keys = [0]

    while keys:
        box = keys.pop()

        for key in boxes[box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == len(boxes)
