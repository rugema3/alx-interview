#!/usr/bin/python3
"""0-validate_utf8 module."""


def validUTF8(data):
    """Check if dataset is a valid utf-8."""
    try:
        for num in data:
            # Check if integer is within a valid range
            if num < 0 or num > 255:
                return False
        bytes_data = bytes(data)
        bytes_data.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
