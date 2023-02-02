class Colours:
    # RGB Colours
    red = [255, 0, 0]
    green = [0, 255, 0]
    blue = [0, 0, 255]

    # Black and White Colours
    white = [255, 255, 255]
    black = [0, 0, 0]

    # Mixes of RGB Colours
    yellow = [255, 255, 0]

    # Colours of Elements
    block = [200, 200, 200]
    interacted_block = [40, 255, 40]
    back = [100, 100, 100]

    # Custom Colours
    custom = {}

    def create_colour(self, red: int, green: int, blue: int, name: str = None):
        colour = [red, green, blue]

        if name is not None:
            Colours.custom[name] = colour.copy()

        return colour
