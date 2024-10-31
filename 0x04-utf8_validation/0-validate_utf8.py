#!/usr/bin/python3
"""NOthing to import"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers representing data bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes remaining in the current UTF-8 character sequence
    num_bytes = 0

    # Masks to check the leading bits of each byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Only need the last 8 bits of each integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # For 1-byte character, num_bytes should be 0
            if num_bytes == 0:
                continue

            # UTF-8 characters must be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease num_bytes by 1 for each byte in the sequence
        num_bytes -= 1

    # All characters should complete at the end
    return num_bytes == 0
