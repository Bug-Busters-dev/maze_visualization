
input = "data\\labyrinthe0.txt"

with open(input, "r") as file:
    lines = file.readlines()
    (x, y) = lines[0].split(" ")
    y = int(y)
    x = int(x)

red =   "255 0   0   "
white = "255 255 255 "
schwarz = "0   0   0   "
grün =  "0   255 0   "

maze1 = [[[[white for _ in range(3)]for _ in range(3)] for _ in range(y)]for _ in range(x)]
print(len(maze1), len(maze1[0]))

def render_4d_list(data):
    x = len(data)
    y = len(data[0])
    
    output_lines = []

    # Für jede Zeile im Gesamtbild (also jedes 3x3-Feld in y-Richtung)
    for j in range(y):
        for sub_row in range(3):  # Für jede Zeile im 3x3-Feld
            line = []
            for i in range(x):
                row = data[i][j][sub_row]  # Die entsprechende Subzeile aus dem 3x3 Feld
                line.extend(row)
            output_lines.append(" ".join(line))  # Zeile als String mit Leerzeichen zwischen RGB-Werten

    return "\n".join(output_lines)



maze_description_len = 2*y-1
number_traps = int(lines[maze_description_len+1])

traps = [[int(part.replace("\n", "")) for part in trap.split(" ")] for trap in lines[maze_description_len+2:maze_description_len+2+number_traps]]

# Zeile, ab der die Wände beginnen
start_line = 1  # Beispiel: Wände beginnen in der zweiten Zeile (Index 1)

# Einlesen der vertikalen Wände: m Zeilen mit n-1 Einträgen
walls_v = [[int(lines[start_line + i].split(" ")[j]) for j in range(x-1)] for i in range(y)]

# Einlesen der horizontalen Wände: m-1 Zeilen mit n Einträgen
walls_h = [[int(lines[start_line + y + i].split(" ")[j]) for j in range(x)] for i in range(y-1)]

# Formatieren der Wände
formatted_walls_v = [[walls_v[j][i] for j in range(y)] for i in range(x-1)] + [[1 for _ in range(y)]]
formatted_walls_h = [[walls_h[j][i] for j in range(y-1)] + [1] for i in range(x)]

# Ausgabe der formatierten Wände
print("Vertikale Wände:", formatted_walls_v)
print("Horizontale Wände:", formatted_walls_h)

for i in range(x):
    for j in range(y):
        if formatted_walls_v[i][j] == 1:
            maze1[i][j][0][2] = schwarz
            maze1[i][j][1][2] = schwarz
            maze1[i][j][2][2] = schwarz
        if formatted_walls_h[i][j] == 1:
            maze1[i][j][2][0] = schwarz
            maze1[i][j][2][1] = schwarz
            maze1[i][j][2][2] = schwarz
            
formatted_traps = [[ 0 for _ in range(y)] for _ in range(x)]

for i,j in traps:
    maze1[i][j][1][1] = red
    maze1[i][j][0][0] = red
    maze1[i][j][2][0] = red
    maze1[i][j][0][2] = red
    maze1[i][j][2][2] = red
    formatted_traps[i][j] = 1
    
pfad = "||>^^>||"

last_x = 0
last_y = 0
akk_x = 0
akk_y = 0

for i in pfad:
    if i == "^":
        if akk_y > 0:
            if formatted_walls_h[akk_x][akk_y-1] == 0:
                if formatted_traps[akk_x][akk_y-1] == 1:
                    last_x = akk_x
                    last_y = akk_y
                    maze1[akk_x][akk_y-1][1][0] = red
                    maze1[akk_x][akk_y-1][0][1] = red
                    maze1[akk_x][akk_y-1][1][2] = red
                    maze1[akk_x][akk_y-1][2][1] = red
                    akk_y = 0
                    akk_x = 0
                else:
                    last_x = akk_x
                    last_y = akk_y
                    maze1[akk_x][akk_y][1][1] = grün
                    maze1[akk_x][akk_y][0][1] = grün
                    maze1[akk_x][akk_y-1][2][1] = grün
                    akk_y -= 1
    elif i == ">":
        if formatted_walls_v[akk_x][akk_y] == 0:
            if formatted_traps[akk_x+1][akk_y] == 1:
                last_x = akk_x
                last_y = akk_y
                maze1[akk_x+1][akk_y][1][0] = red
                maze1[akk_x+1][akk_y][0][1] = red
                maze1[akk_x+1][akk_y][1][2] = red
                maze1[akk_x+1][akk_y][2][1] = red
                akk_x = 0
                akk_y = 0
            else:
                last_x = akk_x
                last_y = akk_y
                maze1[akk_x][akk_y][1][1] = grün
                maze1[akk_x][akk_y][1][2] = grün
                maze1[akk_x+1][akk_y][1][0] = grün
                akk_x += 1
    elif i == "|":
        if formatted_walls_h[akk_x][akk_y] == 0:
            if formatted_traps[akk_x][akk_y+1] == 1:
                last_x = akk_x
                last_y = akk_y
                maze1[akk_x][akk_y+1][1][0] = red
                maze1[akk_x][akk_y+1][0][1] = red
                maze1[akk_x][akk_y+1][1][2] = red
                maze1[akk_x][akk_y+1][2][1] = red
                akk_x = 0
                akk_y = 0
            else:
                last_x = akk_x
                last_y = akk_y
                maze1[akk_x][akk_y][1][1] = grün
                maze1[akk_x][akk_y][2][1] = grün
                maze1[akk_x][akk_y+1][0][1] = grün
                akk_y += 1
    elif i == "<":
        if akk_x > 0:
            if formatted_walls_v[akk_x-1][akk_y] == 0:
                if formatted_traps[akk_x-1][akk_y] == 1:
                    last_x = akk_x
                    last_y = akk_y
                    maze1[akk_x-1][akk_y][1][0] = red
                    maze1[akk_x-1][akk_y][0][1] = red
                    maze1[akk_x-1][akk_y][1][2] = red
                    maze1[akk_x-1][akk_y][2][1] = red
                    akk_x = 0
                    akk_y = 0
                else:
                    last_x = akk_x
                    last_y = akk_y
                    maze1[akk_x][akk_y][1][1] = grün
                    maze1[akk_x][akk_y][1][0] = grün
                    maze1[akk_x-1][akk_y][1][2] = grün
                    akk_x -= 1



with open(f"mazes\\{input[4:16]}_maze.ppm", "w") as file:
    string = ""
    file.write("P3\n")
    file.write(f"{3*x} {3*y}\n")
    file.write("255\n")


    file.write(render_4d_list(maze1))
