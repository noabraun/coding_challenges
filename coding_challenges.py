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


def find_range(lst):
    """Find the smallest and largest number in a list. """
    lst = sorted(lst)

    print "Smallest:"
    print lst[0]
    print "Largest:"
    print lst[-1]


def more_vowels(word):
    """Given a word, return True if it has more vowels than consonants."""

    vowels = ['a', 'e', 'i', 'o', 'u']

    vowel_count = 0
    cons_count = 0

    for letter in word: 
        if letter in vowels:
            vowel_count += 1
        else: 
            cons_count += 1

    if vowel_count > cons_count: 
        return True
    else: 
        return False

















