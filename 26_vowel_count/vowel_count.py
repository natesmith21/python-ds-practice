def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    # showing a vowel count not in alpah order seems odd 
    
    vowels = 'aeiou'
    lower_phrase = phrase.lower()
    vowel_counter = {}

    # {char: count for char in phrase if char  }

    for char in vowels:
        vowel_count = lower_phrase.count(char)
        vowel_counter.update({char: vowel_count})
    return vowel_counter
