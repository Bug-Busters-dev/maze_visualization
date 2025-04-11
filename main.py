
with open("data\\labyrinthe1.txt", "r") as file:
    lines = file.readlines()
    (x, y) = lines[0].split(" ")
    y = int(y)
    x = int(x)

red =   "255 0   0   "
white = "255 255 255 "
schwarz = "0   0   0   "

maze1 = [[[[white for i in range(3)]for i in range(3)] for i in range(y)]for i in range(x)]
print(len(maze1), len(maze1[0]))

def render_4d_list(data):
    output = ""

    for block in data:  # Erste Dimension
        block_rows = [""] * len(block[0])  # 3 Zeilen pro Block

        for row in block:  # Zweite Dimension
            for i, col in enumerate(row):  # Dritte Dimension – 3 Spalten
                numbers = ' '.join(str(n) for n in col)
                block_rows[i] += numbers + " "  # Die Spalten nebeneinander setzen

        # Zusammenfügen der Zeilen für diesen Block und nach der ersten Dimension einen Zeilenumbruch einfügen
        output += '\n'.join(block_rows) + " \n"

    return output.strip()



maze_description_len = 2*y-1
number_traps = int(lines[maze_description_len+1])

traps = [[int(part.replace("\n", "")) for part in trap.split(" ")] for trap in lines[maze_description_len+2:maze_description_len+2+number_traps]]

walls_v = [[int(lines[i].split(" ")[j].replace("\n", "")) for j in range(x-1)] + [1] for i in range(y)]

walls_h = [[int(lines[i].split(" ")[j].replace("\n", "")) for j in range(x)] for i in range(y-1)] + [[1 for _ in range(y)]]

for i in range(x):
    for j in range(y):
        if walls_v[i][j] == 1:
            maze1[i][j][0][2] = schwarz
            maze1[i][j][1][2] = schwarz
            maze1[i][j][2][2] = schwarz
        if walls_h[i][j] == 1:
            maze1[i][j][2][0] = schwarz
            maze1[i][j][2][1] = schwarz
            maze1[i][j][2][2] = schwarz

for x,y in traps:
    maze1[x][y][1][1] = red
    maze1[x][y][0][0] = red
    maze1[x][y][2][0] = red
    maze1[x][y][0][2] = red
    maze1[x][y][2][2] = red



with open("ouput_maze.ppm", "w") as file:
    string = ""
    file.write("P3\n")
    file.write(f"{y*3} {x*3}\n")
    file.write("255\n")


    file.write(render_4d_list(maze1))
