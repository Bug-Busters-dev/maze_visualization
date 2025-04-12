# maze_visualization

This project visualizes mazes and paths through them using a custom rendering system. It processes input files describing the maze structure and generates a visual representation in PPM format.

## Purpose

This script is a custom renderer for the [A2_Simultane-Labyrinthe](https://github.com/Apfelholz/A2_Simultane-Labyrinthe) project and is used to visualize its output.

## Usage

Run the script with the following command:

```bash
python maze_visualization.py <input_file_path> <path_sequence>
```

- `<input_file_path>`: Path to the input file describing the maze.
- `<path_sequence>`: Sequence of moves through the maze (e.g., `||>^^>||`).

If no arguments are provided, the script uses default values:
- Input file: `data\labyrinthe0.txt`
- Path sequence: `||>^^>||`

## Output

The script generates a PPM image file representing the maze and the path. The output file is saved in the `mazes` directory with a name based on the input file.

## Example

Given an input file `data\labyrinthe0.txt` and a path sequence `||>^^>||`, run:

```bash
python maze_visualization.py data\labyrinthe0.txt ||>^^>||
```

The output will be saved as `mazes\labyrinthe0_maze.ppm`.

## Input File Format

The input file should describe the maze structure, including dimensions, walls, and traps. Refer to the example input file for details.

## Dependencies

- Python 3.x