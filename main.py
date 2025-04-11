
with open("data\labyrinthe0.txt", "r") as file:
    lines = file.readlines()
    (m, n) = lines[0].split(" ")
    m = int(m)
    n = int(n)

red =   "255 0   0   "
white = "255 255 255 "
schwarz = "0   0   0   "

maze1 = [[[[white for i in range(3)]for i in range(3)] for i in range(n)]for i in range(m)]
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



maze_description_len = 2*m-1
number_mazes = int(lines[maze_description_len+1])

traps = [[int(part.replace("\n", "")) for part in trap.split(" ")] for trap in lines[maze_description_len+2:maze_description_len+2+number_mazes]]

for x,y in traps:
    maze1[x][y][1][1] = red
    maze1[x][y][0][0] = red
    maze1[x][y][2][0] = red
    maze1[x][y][0][2] = red
    maze1[x][y][2][2] = red
    maze1[x][y][1][0] = schwarz
    maze1[x][y][2][1] = schwarz
    maze1[x][y][1][2] = schwarz
    maze1[x][y][0][1] = schwarz



with open("ouput_maze.ppm", "w") as file:
    string = ""
    file.write("P3\n")
    file.write(f"{m*3} {n*3}\n")
    file.write("255\n")


    file.write(render_4d_list(maze1))
