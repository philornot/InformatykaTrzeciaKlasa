def load_line(line_number, file='../../../matura2024maj/dane2024maj/liczby_przyklad.txt'):
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()
    return lines[line_number - 1]


def line_to_list(line_number):
    line_list = []
    line = load_line(line_number).split(" ")
    for char in line:
        char = int(char)
        line_list.append(char)
    return line_list
