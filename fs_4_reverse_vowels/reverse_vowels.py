def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    new_phrase = ''

    vowel_list = [char for char in s if char in vowels]
    vowel_list = vowel_list[len(vowel_list)::-1]

    for char in s:
        x = s.index(char)
        if char in vowels:
            new_phrase = new_phrase + vowel_list[0]
            vowel_list.remove(vowel_list[0])
        else:
            new_phrase = new_phrase + char
    
    return new_phrase
            



    