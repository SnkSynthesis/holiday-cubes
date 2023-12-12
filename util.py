def rgb255_to_rgb1(r, g, b):
    """
    Converts RGB values that are in the format (255, 255, 255)
    to the format (1.0, 1.0, 1.0)
    """
    return (r / 255, g / 255, b / 255)
