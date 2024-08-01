def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = []

    for char in phrase:
        if char.casefold() == to_swap.casefold():
            new_phrase.append(char.swapcase())
        else: 
            new_phrase.append(char)
    return ''.join(new_phrase)
