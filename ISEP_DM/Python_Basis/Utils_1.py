def solve_quadratic(a: int, b: int, c: int) -> list:
    """
    Solve a quadratic equation of the form ax^2 + bx + c = 0.

    Parameters:
        a (int): Coefficient of the quadratic term.
        b (int): Coefficient of the linear term.
        c (int): Constant term.

    Returns:
        list: A list containing the roots of the quadratic equation.

    Raises:
        ValueError: If the discriminant (delta) is negative, indicating no real roots.

    Examples:
        >>> solve_quadratic(1, -3, 2)
        [1.0, 2.0]

        >>> solve_quadratic(1, 2, 1)
        [-1.0]

    Note:
        The function uses the quadratic formula to find the roots:
        x = (-b ± √(b^2 - 4ac)) / 2a
    """
    delta = b ** 2 - (4 * a * c)

    if delta < 0:
        raise ValueError("No real roots, discriminant is negative.")
    elif delta > 0:
        root1 = (-b - (delta ** 0.5)) / (2 * a)
        root2 = (-b + (delta ** 0.5)) / (2 * a)
        solution = [root1, root2]
    else:
        root = -b / (2 * a)
        solution = [root]

    return solution


def list_biggest(input_list: list) -> float:
    """
    Find the maximum value in a list of 'int' or 'float' values.

    :param input_list: A list of 'int' or 'float' values.
    :return: The maximum value in the input list.
    :raises TypeError: If the input is not a list.
    """

    if isinstance(input_list, list):
        return max(input_list)
    else:
        raise TypeError("Input is not a list!")


def lower_cut_list(input_list) -> list:
    """
    Remove all occurrences of the minimum value from a list of 'int' or 'float' values.

    :param input_list: A list of 'int' or 'float' values.
    :return: A new list with the minimum value removed.
    :raises TypeError: If the input is not a list or if it contains values that are not 'int' or 'float'.
    """

    # Check if input_list is a list
    if isinstance(input_list, list):

        # Check if elements in the list are 'int' or 'float'
        if all(isinstance(i, (int, float)) for i in input_list):

            # Find the minimum value in the list
            lower = min(input_list)

            # Return a new list with the minimum value removed
            return [i for i in input_list if i != lower]

        else:
            raise TypeError("The list contains values that are not 'int' or 'float'!")
    else:
        raise TypeError("Input is not a list!")
