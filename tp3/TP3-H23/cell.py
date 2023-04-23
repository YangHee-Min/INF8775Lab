class Cell:
    def __init__(self, id, up=None, down=None, left=None, right=None):
        self.id = id
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def add_up(self, new_up_cell):
        self.up = new_up_cell

    def add_down(self, new_up_cell):
        self.down = new_up_cell

    def add_left(self, new_up_cell):
        self.left = new_up_cell

    def add_right(self, new_up_cell):
        self.right = new_up_cell
