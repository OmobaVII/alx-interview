#!/usr/bin/python3
"""
This module provides one function `canUnlockAll`
which determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """This function takes a list of lists
    returns True if all boxes can be opened
    otherwise False"""
    keys = [0]
    for k in keys:
        for box_key in boxes[k]:
            if box_key not in keys and box_key < len(boxes):
                keys.append(box_key)
    if len(keys) == len(boxes):
        return True
    else:
        return False
