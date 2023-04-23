from typing import Union
from enum import Enum
import random

TABLE_WIDTH = 5
TABLE_HEIGHT = 5


class Direction(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4


def generate_enclosures():
    table = generate_field(TABLE_WIDTH, TABLE_HEIGHT)
    table = generate_enclosure(0, 0, 0, 0, 25, table)
    return table


def generate_enclosure(start_row, start_column, enclosure_id, current_size, max_size, table):
    # find a way to keep all of the points and

    start_coords = (start_row, start_column)
    enclosure_coords = []

    (row, col) = start_coords
    while current_size < max_size:
        if table[row][col] != None:
            print(
                f'overwriting {table[row][col]} with {enclosure_id}')

        table[row][col] = enclosure_id
        current_size += 1
        if current_size == max_size:
            return table

        # Find which directions are free then decide which one to go to randomly
        possible_new_coords = get_possible_next_coords(table, row, col)
        # randomly choose one of these
        while len(possible_new_coords) < 1:
            # center table in a bigger table if we're trying to go to a border
            if row == 0 or row == len(table) - 1 or col == 0 or col == len(table[0]) - 1:
                table, row, col = center_new_table(table, row, col)
                possible_new_coords = get_possible_next_coords(table, row, col)
            # choose a random point amongst the points of our already existing points to continue off of in hopes it is an edge
            # TODO: replace with function to find edges of
            else:
                row, col = enclosure_coords[random.randint(
                    0, len(enclosure_coords))]
                possible_new_coords = get_possible_next_coords(
                    table, row, col)

        new_coords_index = 0 if len(possible_new_coords) == 1 else random.randint(
            0, len(possible_new_coords) - 1)
        row, col = possible_new_coords[new_coords_index]
        enclosure_coords.append((row, col))
    return table


def get_possible_next_coords(table, row, col):
    possible_new_coords = []
    for direction in Direction:
        next_coords = get_next_cell_coords(direction, row, col)
        if is_cell_free(table, next_coords[0], next_coords[1]):
            possible_new_coords.append(next_coords)
    return possible_new_coords


def center_new_table(table, row, col):
    row, col = get_centered_coordinates(table, row, col)
    table = center_table_and_double_size(table)
    return (table, row, col)


def center_table_and_double_size(table):
    rows = len(table)
    cols = len(table[0])
    new_rows = rows * 2
    new_cols = cols * 2

    centered_table = [[None for j in range(new_cols)] for i in range(new_rows)]

    start_row = new_rows // 2 - rows // 2
    start_col = new_cols // 2 - cols // 2

    for i in range(rows):
        for j in range(cols):
            centered_table[start_row + i][start_col + j] = table[i][j]
    return centered_table

# Must always call before center_table_and_double_size


def get_centered_coordinates(table, original_row_index, original_col_index):
    rows = len(table)
    cols = len(table[0])
    new_rows = rows * 2
    new_cols = cols * 2

    start_row = new_rows // 2 - rows // 2
    start_col = new_cols // 2 - cols // 2

    new_row = start_row + original_row_index
    new_col = start_col + original_col_index

    return new_row, new_col


def is_cell_free(table, row: int, col: int):
    if row < 0 or col < 0 or row > len(table) - 1 or col > len(table[0]) - 1 or table[row][col] != None:
        return False
    return True


def get_next_cell_coords(direction: Union[Direction, int], row: int, column: int):
    if direction == Direction.LEFT:
        return (row, column - 1 if column - 1 >= 0 else 0)
    elif direction == Direction.UP:
        return (row - 1 if row - 1 >= 0 else 0, column)
    elif direction == Direction.RIGHT:
        return (row, column + 1 if column + 1 < TABLE_WIDTH else TABLE_WIDTH)
    elif direction == Direction.DOWN:
        return (row + 1 if row + 1 < TABLE_HEIGHT else TABLE_HEIGHT, column)


def generate_random_direction():
    direction = random.randint(1, 4)
    return Direction(direction)


def generate_field(width, height):
    return [[None for j in range(width)] for i in range(height)]


def print_table(table):
    # Determine the maximum length of each column
    column_widths = [max(len(str(row[i])) for row in table)
                     for i in range(len(table[0]))]

    # Print each row with aligned columns
    for row in table:
        row_string = ''
        for i, cell in enumerate(row):
            row_string += '{:<{}}'.format(str(cell), column_widths[i] + 1)
        print(row_string.rstrip())


if __name__ == "__main__":
    table = generate_enclosures()
    print("FINAL TABLE")
    print_table(table)
