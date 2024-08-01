def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    
    # my_dict = {}
    # for key in keys:
    #     x = keys.index(key)
    #     my_dict.setdefault(key, None)
    # for val in values: 
    #     y = values.index(val)
    #     if not key[y]:
    #         return my_dict
    #     else: 
    #         my_dict.update({key[y]: val})
    # return my_dict

    # return dict(zip(keys, values))

    from itertools import zip_longest
    if len(keys) >= len(values):
        return {k : v for k, v in zip_longest(keys, values)}
    elif len(values) > len(keys):
        return dict(zip(keys, values))
    



