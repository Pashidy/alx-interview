#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    nbytes = 0

    byte1 = 1 << 7  # 10000000
    byte2 = 1 << 6  # 01000000

    for i in data:
        m = 1 << 7
        if nbytes == 0:
            while m & i:
                nbytes += 1
                m = m >> 1
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (i & byte1 and not (i & byte2)):
                return False
        nbytes -= 1
        return nbytes == 0
