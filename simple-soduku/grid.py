from random import sample


def create_line_coordinates(cell_size: int) -> list[list[tuple]]:
    points = []
    for y in range(1,9):
        #horizoznal lines
        temp = []
        temp.append((0, y*cell_size))
        temp.append((900, y*cell_size))
        points.append(temp)

    for x in range(1,10):
        #horizoznal lines
        temp = []
        temp.append((x * cell_size, 0))
        temp.append((x * cell_size, 900))
        points.append(temp)

    return points


SUB_GRID_SIZE = 3
GRID_SIZE = SUB_GRID_SIZE * SUB_GRID_SIZE

def pattern(row_num: int, col_num: int) -> int:
    return (SUB_GRID_SIZE * (row_num % SUB_GRID_SIZE) + row_num // SUB_GRID_SIZE + col_num) % GRID_SIZE

def shuffle(samp: range) -> int:
    return sample(samp, len(samp))

def create_grid(sub_grid: int) -> list[list]:
    row_base = range(sub_grid)
    rows = [g * sub_grid + r for g in shuffle(row_base) for r in shuffle(row_base)]
    cols = [g * sub_grid + c for g in shuffle(row_base) for c in shuffle(row_base)]
    nums = shuffle(range(1, sub_grid * sub_grid + 1))
    return [[nums[pattern(r,c)] for c in cols] for r in rows]

def remove_numbers(grid: list[list]) -> None:
    num_of_cells = GRID_SIZE * GRID_SIZE
    empties = num_of_cells * 3//5   #diff
    for i in sample(range(num_of_cells), empties):
        grid[i// GRID_SIZE][i % GRID_SIZE] = 0    

class Grid:
    def __init__(self, font):
        self.__cell_size = 100
        self.line_coordinates = create_line_coordinates(self.__cell_size)
        self.game_font = font
        self.grid = create_grid(SUB_GRID_SIZE)
        self.__num_x_offset = 35
        self.__num_y_offset = 12
        remove_numbers(self.grid)
        self.occupied_cells_coords = self.occupied_cells_coords()

    def pre_occupied_cells(self) -> list[tuple]:
        occupied_cells_coords = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid)):
                if(self.get_cell(x,y) != 0):
                    occupied_cells_coords.append((x,y))
        return occupied_cells_coords

    def __draw_lines(self, pg, surface) -> None:
        for index, point in enumerate(self.line_coordinates):
            if(index in [2,5,10,13]):
                pg.draw.line(surface, (255,200,0), point[0], point[1])
            else:
                pg.draw.line(surface, (0,50,0), point[0], point[1])

    def __draw_numbers(self, surface) -> None:
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if(self.get_cell(x,y) != 0): 
                    text_surface = self.game_font.render(str(self.get_cell(x,y)), False, (0,200,255))
                    surface.blit(text_surface, (x * self.__cell_size + self.__num_x_offset, y * self.__cell_size + self.__num_y_offset))

    def draw_all(self, pg, surface):
        self.__draw_lines(pg, surface)
        self.__draw_numbers(surface)

    def get_cell(self, x:int, y:int) -> int:
        return self.grid[y][x]
    
    def set_cell(self, x:int, y:int, value:int) -> None:
        self.grid[y][x] = value

    def show(self):
        for cell in self.grid:
            print(cell)






