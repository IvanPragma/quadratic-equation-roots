from __future__ import annotations

from typing import Union


def calculate_quadratic_equation_roots(a: float, b: float, c: float) -> Union[Union[float, list[float]], None]:
    """Function to calculate quadratic equation roots from
    values of a, b and c.

    Return one root (float) or two roots (list[float]) or None.
    """

    try:
        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            return None
        elif discriminant == 0:
            return -b / (2 * a)
        else:
            discriminant_root = discriminant ** 0.5
            return [
                (-b + discriminant_root) / (2 * a),
                (-b - discriminant_root) / (2 * a),
            ]
    except ZeroDivisionError:
        return None
