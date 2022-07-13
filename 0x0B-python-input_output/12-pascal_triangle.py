#!/usr/bin/python3
"""pascal_triangle module"""


def pascal_triangle(n):
    """The Pascal’s triangle of n.

    Args:
        n (int): the value n of the pascal triangle

    Returns:
        data (list of lists): a list of lists of integers
        representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    else:
        final_list = [[1]]

        for i in range(n - 1):

            start = [1]
            last_element = final_list[-1]

            for j in range(len(last_element)):
                try:
                    start.append(last_element[j] + last_element[j + 1])
                except Exception:
                    pass
            start.append(1)
            final_list.append(start)

        return final_list
