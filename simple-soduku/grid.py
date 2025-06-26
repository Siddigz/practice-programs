
def create_line_coordinates(cell_size: int) -> list[list[tuple]]:
    points = []
    for y in range(1,9):
        temp = []
        temp.append((0, y*cell_size))
        temp.append((900, y*cell_size))
        points.append(temp)


class Grid:
    def __init__(self):
        pass