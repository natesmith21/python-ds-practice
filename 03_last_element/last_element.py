def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

    # duh nate -1 is the last index in python 

    last = len(lst) - 1 

    if lst:
        return lst[last]
    else:
        return None

        