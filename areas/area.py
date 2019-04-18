from math import pi


def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("Type is neither int nor float")
    if r < 0:
        raise ValueError("Invalid value like negatives")
    return pi * (r**2)
