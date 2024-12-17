#%%
import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
#from utils.support import log_time, _877_cache_now, logger, console
#from utils import support
from datetime import datetime
#import numpy as np

#Set day/year global variables
DAY:int = datetime.now().day
YEAR:int = datetime.now().year

########################################################

## AoC 2024 Day 14
### Quit playin', let's run up the M's, Back at it agaaaain, Back at it agaaaain, 

def parse_input(input_text):
    """Parse the input and return list of robots with positions and velocities."""
    robots = []
    for line in input_text.strip().split("\n"):
        position, velocity = line.split("v=")
        px, py = map(int, position.split("=")[1].split(","))
        vx, vy = map(int, velocity.split(","))
        robots.append(((px, py), (vx, vy)))
    return robots

def move_robot(position, velocity, time, width, height):
    """Move a robot for 'time' seconds, wrapping around at grid edges."""
    px, py = position
    vx, vy = velocity
    new_x = (px + vx * time) % width
    new_y = (py + vy * time) % height
    return new_x, new_y

def calculate_quadrants(robots, time, width, height):
    """Calculate the number of robots in each quadrant after 'time' seconds."""
    mid_x, mid_y = width // 2, height // 2
    quadrants = [0, 0, 0, 0]  # Quadrants: Top-left, Top-right, Bottom-left, Bottom-right
    
    for position, velocity in robots:
        new_x, new_y = move_robot(position, velocity, time, width, height)
        
        if new_x == mid_x or new_y == mid_y:
            continue  # Skip robots exactly on the middle row or column
        
        if new_x < mid_x and new_y < mid_y:
            quadrants[0] += 1  # Top-left
        elif new_x > mid_x and new_y < mid_y:
            quadrants[1] += 1  # Top-right
        elif new_x < mid_x and new_y > mid_y:
            quadrants[2] += 1  # Bottom-left
        elif new_x > mid_x and new_y > mid_y:
            quadrants[3] += 1  # Bottom-right
    
    return quadrants

def calculate_safety_factor(input_text):
    """Main function to parse input and compute the safety factor."""
    width, height, time = 101, 103, 100
    robots = parse_input(input_text)
    quadrants = calculate_quadrants(robots, time, width, height)
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count
    return safety_factor

# Example Usage
input_text = """
p=73,39 v=-17,38
p=30,80 v=27,22
p=36,10 v=-86,-24
p=56,22 v=6,-46
p=75,64 v=98,-83
p=78,34 v=33,-38
p=83,88 v=-83,55
p=4,0 v=-48,44
p=45,75 v=42,2
p=27,47 v=75,90
p=75,100 v=-90,-61
p=45,29 v=-36,-76
p=73,64 v=48,-7
p=40,7 v=-87,-62
p=43,35 v=-57,11
p=74,77 v=77,70
p=11,42 v=9,4
p=98,28 v=75,34
p=34,42 v=66,-55
p=15,97 v=2,6
p=26,43 v=57,-72
p=84,24 v=-34,36
p=56,79 v=64,67
p=59,30 v=61,-81
p=94,19 v=68,-20
p=55,9 v=-37,83
p=11,69 v=18,75
p=3,45 v=24,76
p=48,88 v=20,-75
p=10,88 v=-13,59
p=77,66 v=47,36
p=28,46 v=73,88
p=2,6 v=-96,18
p=98,80 v=89,-75
p=1,71 v=-77,62
p=68,99 v=89,-42
p=84,35 v=-10,-8
p=26,102 v=-94,-93
p=44,72 v=-84,-51
p=11,39 v=-56,65
p=78,5 v=-38,-63
p=99,101 v=59,-21
p=87,90 v=-77,27
p=58,38 v=-29,75
p=45,69 v=86,-3
p=74,4 v=44,55
p=23,92 v=-71,44
p=97,70 v=-41,-83
p=55,89 v=-9,70
p=55,99 v=-14,58
p=82,72 v=-75,-60
p=10,90 v=58,-38
p=29,49 v=76,-24
p=25,83 v=-88,40
p=19,3 v=1,52
p=5,40 v=-84,19
p=40,28 v=70,27
p=85,0 v=69,-58
p=72,65 v=39,24
p=52,92 v=-73,90
p=75,6 v=41,94
p=93,79 v=75,51
p=15,35 v=-85,46
"""

result = calculate_safety_factor(input_text)
print("Safety factor after 100 seconds:", result)


#%%
## PART B
########################################################
#%% [markdown]

#PART A Notes
## 
##

#PART B Notes
#
#
