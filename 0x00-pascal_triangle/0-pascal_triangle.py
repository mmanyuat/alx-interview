#!/usr/bin/python3
"""NOthing imported"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the n-th row.

    Pascal's triangle is a triangular array of the binomial coefficients.
    Each number is the sum of the two directly above it.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.
                 Must be a positive integer.

    Returns:
        list: A list of lists where each sublist represents a row of
              Pascal's triangle. If n <= 0, an empty list is returned.

    Example:
        >>> pascal_triangle(5)
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize Pascal's triangle with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        # Create the current row by summing adjacent elements previous row
        row = [1] + [prev_row[j] + prev_row[j + 1] for j
                     in range(len(prev_row) - 1)] + [1]
        triangle.append(row)

    return triangle
