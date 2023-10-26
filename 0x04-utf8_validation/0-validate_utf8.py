#!/usr/bin/python3
"""
This module provides a function `validUTF8` which
validates if the given data is a validUTF8
"""


def validUTF8(data):
    """
    validates if data is a valid UTF8
    If data is a valid UTF8 returns True
    if data is not a valid UTF8 returns False
    """
    # Keeps tracks of the number of bytes in the current character
    number_bytes = 0

    for byte in data:
        # checks if it is a continuation byte
        if number_bytes == 0:
            # checks the start of a character
            if (byte >> 7) == 0:
                number_bytes = 0
            elif (byte >> 5) == 0b110:
                number_bytes = 1
            elif (byte >> 4) == 0b1110:
                number_bytes = 2
            elif (byte >> 3) == 0b11110:
                number_bytes = 3
            else:
                return False
        else:
            # checks if it is a continuation byte
            if (byte >> 6) != 0b10:
                return False
            number_bytes -= 1
    if number_bytes != 0:
        return False

    # if there are unmatched continuation bytes or missing bytes, return False
    return True
