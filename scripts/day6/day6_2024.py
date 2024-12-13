#%%
import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, _877_cache_now, logger, console
from utils import support
from datetime import datetime
import numpy as np
from itertools import cycle
from collections import deque

#Set day/year global variables
DAY:int = datetime.now().day
YEAR:int = datetime.now().year

########################################################


def parse_map(input_map):
    """Parse the input map and find the guard's starting position and direction."""
    direction_map = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    grid = []
    start_position = None
    direction = None
    
    for y, line in enumerate(input_map.strip().split('\n')):
        row = []
        for x, char in enumerate(line):
            row.append(char)
            if char in direction_map:
                start_position = (x, y)
                direction = direction_map[char]
        grid.append(row)
    
    return grid, start_position, direction

def turn_right(direction):
    """Turn the direction 90 degrees to the right."""
    if direction == (0, -1):  # Up
        return (1, 0)  # Right
    elif direction == (1, 0):  # Right
        return (0, 1)  # Down
    elif direction == (0, 1):  # Down
        return (-1, 0)  # Left
    elif direction == (-1, 0):  # Left
        return (0, -1)  # Up

def simulate_guard(grid, start_position, start_direction):
    """Simulate the guard's patrol and count unique visited positions."""
    x, y = start_position
    direction = start_direction
    visited = set()
    visited.add((x, y))
    
    rows, cols = len(grid), len(grid[0])
    
    while True:
        # Calculate the next position
        nx, ny = x + direction[0], y + direction[1]
        
        # Check if the guard moves out of bounds
        if nx < 0 or ny < 0 or nx >= cols or ny >= rows:
            break
        
        # If there's an obstacle, turn right
        if grid[ny][nx] == '#':
            direction = turn_right(direction)
        else:
            # Move forward
            x, y = nx, ny
            visited.add((x, y))
    
    return visited

def count_visited_positions(input_map):
    grid, start_position, start_direction = parse_map(input_map)
    visited = simulate_guard(grid, start_position, start_direction)
    return len(visited)

# Example Input
input_map = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

result = count_visited_positions(input_map)
print("Number of distinct positions visited:", result)



########################################################
#Notes
#PART A Notes
## 
##

#PART B Notes
#
#
# %%
