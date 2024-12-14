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

## AoC 2024 Day 11
### Ready to Cookup, I'm ready I'm ready, I'm Ready to Cookup

from collections import deque

def split_number(num):
    """Splits a number into two halves as strings."""
    num_str = str(num)
    mid = len(num_str) // 2
    return int(num_str[:mid]), int(num_str[mid:])

def blink_stones(stones, blinks):
    """Simulates the behavior of the stones over a given number of blinks."""
    stones = deque(stones)  # Use deque for efficient appending and popping

    for _ in range(blinks):
        new_stones = deque()
        for stone in stones:  # Iterate directly over the deque
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                left, right = split_number(stone)
                new_stones.extend([left, right])  # Use extend for efficiency
            else:
                new_stones.append(stone * 2024)

        stones = new_stones

    return len(stones)


## ALTERNATE VERSION (worked for Part A, so slow for Part B)
# from collections import deque

# def split_number(num):
#     """Split number into two halves as strings."""
#     num_str = str(num)
#     mid = len(num_str) // 2
#     return int(num_str[:mid]), int(num_str[mid:])

# def blink_stones(stones, blinks):
#     """Simulate behavior of stones over given number of blinks."""
#     stones = deque(stones)

#     for _ in range(blinks):
#         new_stones = deque()

#         while stones:
#             stone = stones.popleft()
#             if stone == 0:
#                 new_stones.append(1)
#             elif len(str(stone)) % 2 == 0:
#                 left, right = split_number(stone)
#                 new_stones.append(left)
#                 new_stones.append(right)
#             else:
#                 new_stones.append(stone * 2024)

#         stones = new_stones

#     return len(stones)


### PUZZLE INPUT
initial_stones = [0, 27, 5409930, 828979, 4471, 3, 68524, 170]


# CALCULATE # OF STONES AFTER XX BLINKS
blinks = 25
result = blink_stones(initial_stones.copy(), blinks)
print(f"Number of stones after {blinks} blinks:", result)

# Part A
blinks_partA = 25
result_partA = blink_stones(initial_stones.copy(), blinks_partA)
print(f"Number of stones after {blinks_partA} blinks:", result_partA)

# Part B
blinks_partB = 75
result_partB = blink_stones(initial_stones.copy(), blinks_partB)
print(f"Number of stones after {blinks_partB} blinks:", result_partB)



########################################################
#%% [markdown]

#PART A Notes
## 
##

#PART B Notes
#
#
#%%
