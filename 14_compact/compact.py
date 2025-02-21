def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    true_elem = []
    for item in lst:
        if bool(item) == True:
            true_elem.append(item)
    return true_elem