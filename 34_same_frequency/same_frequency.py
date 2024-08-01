def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num1_str = str(num1)
    num2_str = str(num2)

    for num in num1_str:
        if num1_str.count(str(num)) != num2_str.count(str(num)):
            return False    
    return True
    