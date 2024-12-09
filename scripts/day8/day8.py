#%%
import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
#from utils.support import log_time, _877_cache_now, logger, console
from utils import support
from datetime import datetime
import numpy as np

#Set day/year global variables
DAY:int = datetime.now().day
YEAR:int = datetime.now().year

########################################################

from collections import defaultdict
from itertools import combinations

# Parse the puzzle input into a grid
def parse_input(input_data):
    grid = [list(line) for line in input_data.strip().split('\n')]
    return np.array(grid)

# Find antenna positions grouped by frequency
def find_antennas(grid):
    antennas = defaultdict(list)
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            char = grid[r, c]
            if char.isalnum():  # Consider only antennas (letters or digits)
                antennas[char].append((r, c))
    return antennas

# Calculate antinodes for a pair of antennas
def calculate_antinodes(pair):
    (r1, c1), (r2, c2) = pair
    antinodes = set()
    # Check if perfectly aligned vertically or horizontally
    if r1 == r2:  # Horizontal alignment
        dist = abs(c2 - c1)
        if dist % 2 == 0:
            midpoint = (r1, (c1 + c2) // 2)
            antinodes.add((r1, c1 - dist))
            antinodes.add((r1, c2 + dist))
            antinodes.add(midpoint)
    elif c1 == c2:  # Vertical alignment
        dist = abs(r2 - r1)
        if dist % 2 == 0:
            midpoint = ((r1 + r2) // 2, c1)
            antinodes.add((r1 - dist, c1))
            antinodes.add((r2 + dist, c1))
            antinodes.add(midpoint)
    return antinodes

# Main function to compute unique antinodes
def count_unique_antinodes(grid):
    antennas = find_antennas(grid)
    unique_antinodes = set()
    
    # For each frequency, calculate antinodes
    for frequency, positions in antennas.items():
        for pair in combinations(positions, 2):  # All pairs of antennas
            unique_antinodes.update(calculate_antinodes(pair))
    
    # Filter antinodes within grid bounds and include antenna positions
    rows, cols = grid.shape
    valid_antinodes = {pos for pos in unique_antinodes if 0 <= pos[0] < rows and 0 <= pos[1] < cols}
    antenna_positions = set(pos for positions in antennas.values() for pos in positions)
    
    return len(valid_antinodes.union(antenna_positions))

# Puzzle input
puzzle_input = """
.....y..........................p................r
........I.........................................
......................4.s.........................
..........4.......................................
....y.............................................
......................................p.........r.
..........0..s......N..................1.....p....
..y........4.......................p..............
...............0..................................
..............0....t....N....h....................
.............N....................................
......j...................s............H...l..O...
..........q.................H................O....
..f...e.qj.....y...0..............................
...........t..........................k..Q..r.....
.........6................Q..s...x......W.........
....2..b...e....t..4.........c.....xW.j...........
...e....................w................1.....O..
..e..j..5...........................c.............
.........B..2...............MK................H...
...2......b...g..X...q..........h...............O.
...q...2..........m....k...i...............QV.x...
...................i.........W.k.............HQ...
........b...X...............D..........c...N......
................................l..........h.....I
.m...........g......l.......c.............3......V
....X.......m........g...V.K...7......F.d.........
.........b.X...U..........................C.......
.....................l..............o.1....C......
............u.............K..............3...d....
......................i.T....f................V...
..............................1.k.................
.B.....E......9..m....K..5.M......................
...P...............M...95....o..i........I........
...............................S......3......wI...
.....EP...........9........5..T.R.................
.P..........v..9......f.............R.Co..w3......
..........h...SG..v.E...7..f.T....................
..........6..........L.................Y.......d..
..........B...............U........D..............
....B................U.....8..M....n...J..........
.........................L................Fw......
....L6E.P.................7.UG....J.....Y.D.......
........t........v...SJ........n..d...............
......................8v.....uG...................
..................L.....n.........................
...............T..............n......D............
..............o.........8................J.Y.R....
..................S...............u....F.......R..
........6..............u.....7.8..........Y..F....
"""

# Execution
grid = parse_input(puzzle_input)
result = count_unique_antinodes(grid)
result


########################################################
#Notes
#PART A Notes
## goal:
##

#PART B Notes
#
#
# %%

## Attempted Optimizing (?)

# import numpy as np
# from collections import defaultdict

# # Parse the puzzle input into a grid
# def parse_input(input_data):
#     grid = [list(line) for line in input_data.strip().split('\n')]
#     return np.array(grid)

# # Find antenna positions grouped by frequency
# def find_antennas(grid):
#     antennas = defaultdict(list)
#     for r in range(grid.shape[0]):
#         for c in range(grid.shape[1]):
#             char = grid[r, c]
#             if char.isalnum():  # Consider only antennas (letters or digits)
#                 antennas[char].append((r, c))
#     return antennas

# # Calculate antinodes for a pair of antennas
# def calculate_antinodes(pair):
#     (r1, c1), (r2, c2) = pair
#     if (r1 == r2 or c1 == c2):  # Check if perfectly aligned
#         dr, dc = r2 - r1, c2 - c1
#         midpoint_r, midpoint_c = r1 + dr // 2, c1 + dc // 2
#         if abs(dr) % 2 == 0 and abs(dc) % 2 == 0:  # Ensure midpoint is integer
#             antinode1 = (r1 - dr, c1 - dc)
#             antinode2 = (r2 + dr, c2 + dc)
#             return [antinode1, (midpoint_r, midpoint_c)], [antinode2]  # Return midpoint as tuple
#     return []

# # Main function to compute unique antinodes
# def count_unique_antinodes(grid):
#     antennas = find_antennas(grid)
#     antinodes = set()
#     for char, positions in antennas.items():
#         for pair in itertools.combinations(positions, 2):
#             for antinode in calculate_antinodes(pair):
#                 for point in antinode:  # Iterate over points in the list
#                     if 0 <= point[0] < grid.shape[0] and 0 <= point[1] < grid.shape[1]:  # Check bounds
#                         antinodes.add(point)  # Add tuple directly to set
#     return len(antinodes)

# if __name__ == "__main__":
#     with open("day8_input.txt", "r") as f:
#         input_data = f.read()

#     grid = parse_input(input_data)
#     unique_antinodes_count = count_unique_antinodes(grid)
#     print("Unique Antinode Locations:", unique_antinodes_count)

#%%
