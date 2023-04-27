def generate_txt_file(answer_grid: list, enc_count):
    label_to_coords_map = [[] for i in range(enc_count)]
    for row in range(len(answer_grid)):
        for col in range(len(answer_grid[0])):
            label = answer_grid[row][col]
            if label == None:
                continue
            label_to_coords_map[label].append(row)
            label_to_coords_map[label].append(col)
    file = ""
    for line in label_to_coords_map:
        for i, elem in enumerate(line):
            suffix = " "
            if (i == len(line) - 1):
                suffix = "\n"
            file += (str(elem) + suffix)
    print(file)
