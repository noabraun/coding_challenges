def add_to_zero(lst):
    """Add to zero: Given a list of ints, return 
    True if any two nums in list sum to zero"""

    for num in lst:
        if num*-1 in lst: 
            return True

    return False


def concatenate_lists(lst1, lst2):
    """ Concatenate one list at the end of another """
    new_lst = lst1 + lst2
    return new_lst


def find_lucky_numbers(n, lst):
    """Return n unique random numbers from a list. """

    if n > len(lst):
        return lst

    else:
        return lst[:n]