#!/usr/bin/python3
"""  UTF-8 Validation"""


def validUTF8(data):
    """ validatinf if data is a valid utf-8"""

    for num in data:
        bin_num = f'{num:08b}'
        len_bits = len(bin_num)
        if len_bits == 8 and bin_num[0] != "0":
            return False
        if len_bits > 8 and bin_num[-8:-6] != "10":
            return False

    return True
