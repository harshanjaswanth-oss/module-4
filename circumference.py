import math

def circumference(radius):
    """Return the circumference of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * math.pi * radius

