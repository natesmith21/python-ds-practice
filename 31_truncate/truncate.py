def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    ph_len = len(phrase)
    trim_n = n - 3
    ellipsis = '...'
    trimmed_phrase = phrase[0: trim_n]
    
    if n <= ph_len and trim_n >= 0:
        return trimmed_phrase + ellipsis
    elif n > ph_len:
        return phrase
    elif trim_n < 0: 
        return 'Truncation must be at least 3 characters.'



