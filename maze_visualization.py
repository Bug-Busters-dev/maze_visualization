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

# Adjust maze1 to handle two mazes with a gap
maze1 = [[[[white for _ in range(3)] for _ in range(3)] for _ in range(y)] for _ in range(2 * x + 2)]

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
                maze1[i + offset_x][j][0][2] = schwarz
                maze1[i + offset_x][j][1][2] = schwarz
                maze1[i + offset_x][j][2][2] = schwarz
            if formatted_walls_h[i][j] == 1:
                maze1[i + offset_x][j][2][0] = schwarz
                maze1[i + offset_x][j][2][1] = schwarz
                maze1[i + offset_x][j][2][2] = schwarz

    # Draw traps
    formatted_traps = [[0 for _ in range(y)] for _ in range(x)]
    for i, j in traps:
        maze1[i + offset_x][j][1][1] = red
        maze1[i + offset_x][j][0][0] = red
        maze1[i + offset_x][j][2][0] = red
        maze1[i + offset_x][j][0][2] = red
        maze1[i + offset_x][j][2][2] = red
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

# Process the first maze and draw the path
next_start_line, formatted_walls_h, formatted_walls_v, formatted_traps = process_maze(1, 0)
draw_path(pfad, formatted_walls_h, formatted_walls_v, formatted_traps, maze1, 0)

# Process the second maze and draw the path
next_start_line, formatted_walls_h, formatted_walls_v, formatted_traps = process_maze(next_start_line, x + 2)
draw_path(pfad, formatted_walls_h, formatted_walls_v, formatted_traps, maze1, x + 2)

# Adjust rendering to include the gap
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

# Update output dimensions to account for the gap
with open(f"mazes\\{input[4:16]}_maze.ppm", "w") as file:
    file.write("P3\n")
    file.write(f"{3 * (2 * x + 2)} {3 * y}\n")
    file.write("255\n")
    file.write(render_4d_list(maze1))
