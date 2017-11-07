def add_to_zero(lst):
    """Add to zero: Given a list of ints, return 
    True if any two nums in list sum to zero"""

    for num in lst:
        if num*-1 in lst: 
            return True

    return False
