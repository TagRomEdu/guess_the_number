def is_valid(string):
    """
    Check the string is integer number
    """
    return string.isdigit() and 0 < int(string) < 101
