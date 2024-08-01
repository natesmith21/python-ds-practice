def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    to_sum = []
    y = -1

    for lst in matrix:
        x = matrix.index(lst)
        to_sum.append(lst[x])
        to_sum.append(lst[y])
        # print(f'(x,y) = {lst[x], lst[y]}')
        y+= -1
    return sum(to_sum)

        # to_sum = []

    # for lst in matrix:
    #     x = matrix.index(lst)
    #     y = (len(matrix) - x) - 1 
    #     print(f' (x, y) = {x, y}')
    #     print(f'{lst[x], lst[-y]}')
    #     to_sum.append(lst[x])
    #     to_sum.append(lst[-y])


    

