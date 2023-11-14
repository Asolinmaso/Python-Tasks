def draw_horizontal_line(size):
    print(" ---" * size)

def draw_vertical_line(size):
    print("|   " * (size + 1))

def draw_grid(grid_size):
    for _ in range(grid_size):
        draw_horizontal_line(grid_size)
        draw_vertical_line(grid_size)
    draw_horizontal_line(grid_size)  

grid_size = 3  
draw_grid(grid_size)
