def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    count_left = 0
    count_right = 0
    
    for char in parens:
        if char == '(':
            count_left+= 1
        elif char == ')':
            count_right+=1
            if count_right > count_left:
                return False
    if parens.count('(') == parens.count(')'):
        return True
    else:
        return False