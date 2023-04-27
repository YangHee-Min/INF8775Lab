def generate_txt_file(answer_grid: list, enc_count):
    label_to_coords_map = [[] for i in range(enc_count)]
    for row in range(len(answer_grid)):
        for col in range(len(answer_grid[0])):
            label = answer_grid[row][col]
            if label == None:
                continue
            label_to_coords_map[label].append(row)
            label_to_coords_map[label].append(col)
    print()
    for line in label_to_coords_map:
        line_string = ""
        for i, elem in enumerate(line):
            suffix = " "
            if (i == len(line) - 1):
                suffix = ""
            line_string += (str(elem) + suffix)
        print(line_string)
