class Area:
    def __init__(self, area):
        self.block_char = "#"
        self.area = [list(row) for row in area]
        """self.width = len(self.area[-1])
        self.height = len(self.area)
        self.block_width = """
