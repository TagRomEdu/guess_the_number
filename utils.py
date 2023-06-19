def is_valid(string, n):
    """
    Check the string is integer number
    """
    return string.isdigit() and 0 < int(string) < int(n)
