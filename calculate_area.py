def calculate_area(length, width=None):
    # docstring are used to describe what a function does, useful for documentatio
    """Calculate the area of a rectangle or square."""
    if width is None:  # If width is not provided, it's a square
        return length * length
    return length * width


print(calculate_area(5, 3))  # Rectangle: Output: 15
print(calculate_area(4))  # Square: Output: 16
