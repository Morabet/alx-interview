#!/usr/bin/python3
'''UTF-8 Validation'''


from typing import List


def validUTF8(data: List[int]) -> bool:
    '''validating if a set of data is a valid utf-8'''

    # will count how many more byte needed in case
    # of more than one byte character
    byte_needed = 0

    for number in data:
        if byte_needed == 0:

            if number >> 5 == 0b110 or number >> 5 == 0b1110:
                byte_needed = 1

            elif number >> 4 == 0b1110:
                byte_needed = 2

            elif number >> 3 == 0b11110:
                byte_needed = 3

            elif number >> 7 == 0b1:
                # invalid case if only one byte and msb = 1
                # ! all one byte values that start with 0 are valid
                return False

        else:
            # if more than one byte then 2 msb must be '10'
            if number >> 6 != 0b10:
                return False

            byte_needed -= 1

    # return True
    # if data contains a single and only one byte long
    # if in case more than one byte, and has sufficient and valid bytes
    return byte_needed == 0
