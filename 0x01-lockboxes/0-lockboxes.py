#!/usr/bin/python3
'''
Write a method that determines if all the boxes can be opened.
'''


def getkeys(boxes, keys):
    '''a recursive function to get all the keys in opened boxes'''
    updated_keys = set()
    updated_keys.update(keys)
    set_init_size = len(updated_keys)

    for k in keys:
        if k < len(boxes):
            updated_keys.update(boxes[k])

    if set_init_size != len(updated_keys):
        return getkeys(boxes, updated_keys)

    return updated_keys


def canUnlockAll(boxes):
    '''check if all boxes can be opened'''
    if len(boxes) == 0:
        return False

    keys = getkeys(boxes, [0])

    for i in range(len(boxes)):
        if i not in keys:
            return False

    return True
