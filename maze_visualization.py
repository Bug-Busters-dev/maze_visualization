import sys

# python maze_visualization.py <Pfad_zur_Eingabedatei> <Pfadfolge>

# Standardwerte
input = "data\\labyrinthe0.txt"
pfad = "||>^^>||"

if len(sys.argv) > 1:
    input = sys.argv[1]
if len(sys.argv) > 2:
    pfad = sys.argv[2]

with open(input, "r") as file:
    lines = file.readlines()
    (x, y) = lines[0].split(" ")
    y = int(y)
    x = int(x)

red =   "255 0   0   "
white = "255 255 255 "
schwarz = "0   0   0   "
grün =  "0   255 0   "
mintgrün = "0   255 255 "
pink =  "255 0   255 "

# Adjust maze to handle two mazes with a gap
maze = [[[[white for _ in range(3)] for _ in range(3)] for _ in range(y)] for _ in range(2 * x + 2)]

# Update process_maze to return formatted walls and traps
def process_maze(start_line, offset_x):
    walls_v = [[int(lines[start_line + i].split(" ")[j]) for j in range(x-1)] for i in range(y)]
    walls_h = [[int(lines[start_line + y + i].split(" ")[j]) for j in range(x)] for i in range(y-1)]
    number_traps = int(lines[start_line + 2 * y - 1])
    traps = [[int(part.replace("\n", "")) for part in trap.split(" ")] for trap in lines[start_line + 2 * y:number_traps + start_line + 2 * y]]

    # Format walls
    formatted_walls_v = [[walls_v[j][i] for j in range(y)] for i in range(x-1)] + [[1 for _ in range(y)]]
    formatted_walls_h = [[walls_h[j][i] for j in range(y-1)] + [1] for i in range(x)]

    # Draw walls
    for i in range(x):
        for j in range(y):
            if formatted_walls_v[i][j] == 1:
                maze[i + offset_x][j][0][2] = schwarz
                maze[i + offset_x][j][1][2] = schwarz
                maze[i + offset_x][j][2][2] = schwarz
            if formatted_walls_h[i][j] == 1:
                maze[i + offset_x][j][2][0] = schwarz
                maze[i + offset_x][j][2][1] = schwarz
                maze[i + offset_x][j][2][2] = schwarz
                
    # Draw borders
    for i in range(x):
        maze[i + offset_x][0][0][0] = schwarz
        maze[i + offset_x][0][0][1] = schwarz
        maze[i + offset_x][0][0][2] = schwarz
    
    for j in range(y):
        maze[0 + offset_x][j][0][0] = schwarz
        maze[0 + offset_x][j][1][0] = schwarz
        maze[0 + offset_x][j][2][0] = schwarz
        
 
    # Draw traps
    formatted_traps = [[0 for _ in range(y)] for _ in range(x)]
    for i, j in traps:
        maze[i + offset_x][j][1][1] = red
        maze[i + offset_x][j][0][0] = red
        maze[i + offset_x][j][2][0] = red
        maze[i + offset_x][j][0][2] = red
        maze[i + offset_x][j][2][2] = red
        formatted_traps[i][j] = 1

    return start_line + 2 * y + number_traps, formatted_walls_h, formatted_walls_v, formatted_traps

def draw_path(pfad, formatted_walls_h, formatted_walls_v, formatted_traps, maze1, offset_x):
    akk_x = 0
    akk_y = 0

    for i in pfad:
        if i == "^":
            if akk_y > 0:
                if formatted_walls_h[akk_x][akk_y-1] == 0:
                    if formatted_traps[akk_x][akk_y-1] == 1:
                        maze1[akk_x + offset_x][akk_y-1][1][0] = red
                        maze1[akk_x + offset_x][akk_y-1][0][1] = red
                        maze1[akk_x + offset_x][akk_y-1][1][2] = red
                        maze1[akk_x + offset_x][akk_y-1][2][1] = red
                        akk_y = 0
                        akk_x = 0
                    else:
                        maze1[akk_x + offset_x][akk_y][1][1] = grün
                        maze1[akk_x + offset_x][akk_y][0][1] = grün
                        maze1[akk_x + offset_x][akk_y-1][2][1] = grün
                        akk_y -= 1
        elif i == ">":
            if formatted_walls_v[akk_x][akk_y] == 0:
                if formatted_traps[akk_x+1][akk_y] == 1:
                    maze1[akk_x+1 + offset_x][akk_y][1][0] = red
                    maze1[akk_x+1 + offset_x][akk_y][0][1] = red
                    maze1[akk_x+1 + offset_x][akk_y][1][2] = red
                    maze1[akk_x+1 + offset_x][akk_y][2][1] = red
                    akk_x = 0
                    akk_y = 0
                else:
                    maze1[akk_x + offset_x][akk_y][1][1] = grün
                    maze1[akk_x + offset_x][akk_y][1][2] = grün
                    maze1[akk_x+1 + offset_x][akk_y][1][0] = grün
                    akk_x += 1
        elif i == "|":
            if formatted_walls_h[akk_x][akk_y] == 0:
                if formatted_traps[akk_x][akk_y+1] == 1:
                    maze1[akk_x + offset_x][akk_y+1][1][0] = red
                    maze1[akk_x + offset_x][akk_y+1][0][1] = red
                    maze1[akk_x + offset_x][akk_y+1][1][2] = red
                    maze1[akk_x + offset_x][akk_y+1][2][1] = red
                    akk_x = 0
                    akk_y = 0
                else:
                    maze1[akk_x + offset_x][akk_y][1][1] = grün
                    maze1[akk_x + offset_x][akk_y][2][1] = grün
                    maze1[akk_x + offset_x][akk_y+1][0][1] = grün
                    akk_y += 1
        elif i == "<":
            if akk_x > 0:
                if formatted_walls_v[akk_x-1][akk_y] == 0:
                    if formatted_traps[akk_x-1][akk_y] == 1:
                        maze1[akk_x-1 + offset_x][akk_y][1][0] = red
                        maze1[akk_x-1 + offset_x][akk_y][0][1] = red
                        maze1[akk_x-1 + offset_x][akk_y][1][2] = red
                        maze1[akk_x-1 + offset_x][akk_y][2][1] = red
                        akk_x = 0
                        akk_y = 0
                    else:
                        maze1[akk_x + offset_x][akk_y][1][1] = grün
                        maze1[akk_x + offset_x][akk_y][1][0] = grün
                        maze1[akk_x-1 + offset_x][akk_y][1][2] = grün
                        akk_x -= 1
                        
def draw_start_and_end(maze, x, y, offset_x, start_coords, end_coords):
    start_x, start_y = start_coords
    end_x, end_y = end_coords

    # Draw start
    maze[start_x + offset_x][start_y][1][1] = pink
    maze[start_x + offset_x][start_y][1][0] = pink
    maze[start_x + offset_x][start_y][1][2] = pink
    maze[start_x + offset_x][start_y][0][1] = pink
    maze[start_x + offset_x][start_y][2][1] = pink

    # Draw end
    maze[end_x + offset_x][end_y][1][1] = mintgrün
    maze[end_x + offset_x][end_y][1][0] = mintgrün
    maze[end_x + offset_x][end_y][1][2] = mintgrün
    maze[end_x + offset_x][end_y][0][1] = mintgrün
    maze[end_x + offset_x][end_y][2][1] = mintgrün


# Process the first maze and draw the path
next_start_line, formatted_walls_h, formatted_walls_v, formatted_traps = process_maze(1, 0)
draw_path(pfad, formatted_walls_h, formatted_walls_v, formatted_traps, maze, 0)

# Process the second maze and draw the path
next_start_line, formatted_walls_h, formatted_walls_v, formatted_traps = process_maze(next_start_line, x + 2)
draw_path(pfad, formatted_walls_h, formatted_walls_v, formatted_traps, maze, x + 2)

if len(lines) > next_start_line:
    start_coords = [int(lines[next_start_line].split(" ")[0]), int(lines[next_start_line].split(" ")[1])]
    end_coords = [int(lines[next_start_line + 1].split(" ")[0]), int(lines[next_start_line + 1].split(" ")[1])]

    # Draw start and end points
    draw_start_and_end(maze, x, y, 0, start_coords, end_coords)
    draw_start_and_end(maze, x, y, x + 2, start_coords, end_coords)
else:
    start_coords = [0, 0]
    end_coords = [x-1, y-1]
    draw_start_and_end(maze, x, y, 0, start_coords, end_coords)
    draw_start_and_end(maze, x, y, x + 2, start_coords, end_coords)

def render_4d_list(data):
    x = len(data)
    y = len(data[0])
    
    output_lines = []

    for j in range(y):
        for sub_row in range(3):
            line = []
            for i in range(x):
                row = data[i][j][sub_row]
                line.extend(row)
            output_lines.append(" ".join(line))

    return "\n".join(output_lines)

with open(f"mazes\\{input[4:16]}_maze.ppm", "w") as file:
    file.write("P3\n")
    file.write(f"{3 * (2 * x + 2)} {3 * y}\n")
    file.write("255\n")
    file.write(render_4d_list(maze))
