from read_values import read_file
from typing import Union
from enum import Enum
import random
from typing import Dict

TABLE_WIDTH = 5
TABLE_HEIGHT = 5


class StuckException(Exception):
    def __init__(self, message="Stuck in circled area that will always be too small. Aborting"):
        self.message = message
        super().__init__(self.message)


class Direction(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4


def generate_enclosures(id_to_size_map: Dict[int, int]):
    table = generate_field(TABLE_WIDTH, TABLE_HEIGHT)
    row, col = get_center_coord(len(table[0]), len(table))

    for id in id_to_size_map:
        enclosureIsSet = False
        while not enclosureIsSet:
            try:
                table = generate_enclosure(
                    start_row=row, start_column=col, enclosure_id=id, max_size=id_to_size_map[id], table=table)
                enclosureIsSet = True
            except StuckException:
                # if not enough space: clear and reset table
                remove_value(table, id)
                # check border values
                # if filled too much then double in size
                if isFilledOverCapacity(table, id_to_size_map[id]):
                    table = center_table_and_double_size(table)
                # get none None border
                border_coords_same_id = get_edges(table)
                # if boorder_coords_same_id is Empty it means we have the Empty 2d array. Just center it and go next.
                if len(border_coords_same_id) < 1:
                    row, col = get_center_coord(len(table[0]), len(table))
                    continue
                next_coords_list_same_id = get_non_none_border_coords(
                    table, border_coords_same_id)
                index = random.randint(0, len(next_coords_list_same_id) - 1)
                row, col = next_coords_list_same_id[index]

        border_coords = get_edges(table)
        if len(border_coords) < 1:
            table = center_table_and_double_size(table)
            continue
        next_coords_list = get_non_none_border_coords(table, border_coords)
        if len(next_coords_list) < 1:
            table = center_table_and_double_size(table)
            continue
        index = random.randint(
            0, len(next_coords_list) - 1)
        (row, col) = next_coords_list[index]

    return table


def get_non_none_border_coords(table, border_points):
    next_coords_list = []
    for point in border_points:
        next_coords = get_possible_next_coords(
            table, point[0], point[1])
        if len(next_coords) > 0:
            next_coords_list.extend(next_coords)
    return next_coords_list


def isFilledOverCapacity(table, id_size):
    count = 0
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] != None:
                count += 1
    return ((len(table) * len(table[0])) - count) / id_size < 2


def get_center_coord(table_width, table_height):
    center_x = table_width // 2
    center_y = table_height // 2
    return (center_x, center_y)


def remove_value(table, value):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == value:
                table[i][j] = None
    return table


def generate_enclosure(start_row, start_column, enclosure_id, max_size, table):
    # find a way to keep all of the points and
    current_size = 0
    start_coords = (start_row, start_column)

    (row, col) = start_coords
    while current_size < max_size:
        if table[row][col] != None:
            print("OLD:")
            print_table(table)
            print(possible_new_coords)
            raise Exception(f'overwriting {row}x{col} with id {enclosure_id}')

        table[row][col] = enclosure_id
        current_size += 1
        if current_size == max_size:
            return table

        # Find which directions are free then decide which one to go to randomly
        possible_new_coords = get_possible_next_coords(table, row, col)
        old_coords = []
        # randomly choose one of these
        while len(possible_new_coords) < 1:
            if row == 0 or row == len(table) - 1 or col == 0 or col == len(table[0]) - 1:
                table, ref_row, ref_col = center_new_table(table, row, col)
                possible_new_coords = get_possible_next_coords(
                    table, ref_row, ref_col)
            # choose a random point amongst the points of our already existing points to continue off of in hopes it is an edge
            else:
                border_points = get_edges_with_value(table, enclosure_id)
                rand_index = random.randint(
                    0, len(border_points) - 1)
                ref_row, ref_col = border_points[rand_index]
                old_coords = possible_new_coords
                possible_new_coords = get_possible_next_coords(
                    table, ref_row, ref_col)
                if old_coords == possible_new_coords:
                    raise StuckException

        new_coords_index = 0 if len(possible_new_coords) == 1 else random.randint(
            0, len(possible_new_coords) - 1)
        row, col = possible_new_coords[new_coords_index]
    return table


def get_manhattan_distance(tuple1, tuple2):
    return abs(tuple2[0] - tuple1[0]) + abs(tuple2[1] - tuple1[1])


def get_edges(table):
    rows, cols = len(table), len(table[0])
    edge_nodes = []

    # Check each element and its neighbors
    for i in range(rows):
        for j in range(cols):
            if table[i][j] is not None:
                if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                    # Element is on the edge of the array
                    edge_nodes.append((i, j))
                else:
                    # Check if any neighbors are not the target value
                    if not (table[i-1][j] is None and table[i+1][j] is None and table[i][j-1] is None and table[i][j+1] is None):
                        edge_nodes.append((i, j))

    return edge_nodes


def get_edges_with_value(table, value):
    rows, cols = len(table), len(table[0])
    edges = []

    # Check each element and its neighbors
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == value:
                if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                    # Element is on the edge of the array
                    edges.append((i, j))
                else:
                    # Check if any neighbors are not the target value
                    if table[i-1][j] is not value or table[i+1][j] is not value or table[i][j-1] is not value or table[i][j+1] is not value:
                        edges.append((i, j))

    return edges


def get_possible_next_coords(table, row, col):
    possible_new_coords = []
    for direction in Direction:
        next_coords = get_next_cell_coords(
            direction, row, col, len(table[0]), len(table))
        if is_cell_free(table, next_coords[0], next_coords[1]):
            possible_new_coords.append(next_coords)
    return possible_new_coords


def center_new_table(table, row, col):
    new_row, new_col = get_centered_coordinates(
        len(table), len(table[0]), row, col)
    table = center_table_and_double_size(table)
    return (table, new_row, new_col)


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


def get_centered_coordinates(rows: int, cols: int, original_row_index: int, original_col_index: int):
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


def get_next_cell_coords(direction: Union[Direction, int], row: int, column: int, width: int, height: int):
    if direction == Direction.LEFT:
        return (row, column - 1 if column - 1 >= 0 else 0)
    elif direction == Direction.UP:
        return (row - 1 if row - 1 >= 0 else 0, column)
    elif direction == Direction.RIGHT:
        return (row, column + 1 if column + 1 < width else width)
    elif direction == Direction.DOWN:
        return (row + 1 if row + 1 < height else height, column)


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
            value = '-' if cell is None else str(cell)
            row_string += '{:<{}}'.format(value, column_widths[i] + 1)
        print(row_string.rstrip())
    print()


def count_enclosure(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if visited[i][j] or grid[i][j] == None:
            return
        visited[i][j] = True
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    count = 0
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and grid[i][j] != None:
                count += 1
                dfs(i, j)
    return count


def count_all_islands(table, enc_count):
    less_than_1 = []
    more_than_1 = []
    for i in range(enc_count):
        count = count_islands(table, i)
        if count > 1:
            more_than_1.append(i)
        if count < 1:
            less_than_1.append(i)

    more_than_1_str = ""

    less_than_1_str = ""
    exception = False
    if len(less_than_1) > 0:
        less_than_1_str = f'< 1: {less_than_1}\n'
        exception = True
    if len(more_than_1) > 0:
        more_than_1_str = f'< 1: {more_than_1}\n'
        exception = True
    if exception:
        raise Exception(less_than_1_str + more_than_1_str)


def count_islands(grid, label):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if visited[i][j] or grid[i][j] != label:
            return
        visited[i][j] = True
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    count = 0
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and grid[i][j] == label:
                count += 1
                dfs(i, j)
    return count


if __name__ == "__main__":
    (enc_count, m_set_count, min_dist, id_to_size, weights) = read_file(
        "D:/POLY/H2023/INF8775/INF8775Lab/tp3/TP3-H23/n20_m15_V-74779.txt")
    for i in range(200):
        table = generate_enclosures(id_to_size)
        print(f'--------------Completed {i}------------')
        print_table(table)
        print(f'island count: {count_enclosure(table)}')
        count_all_islands(table, enc_count)

    # count_all_islands(table, enc_count)
    # print_table(table)
    # for i in range(1000):
    #     map = {
    #         1: 25,
    #         2: 5,
    #         3: 2,
    #     }
    #     table = generate_enclosures(map)
    #     print("----------------FINAL-------------------")
    #     print_table(table)
    #     numislands = numIslands(table)
    #     if (numislands > 1):
    #         raise Exception("ERROR!")
