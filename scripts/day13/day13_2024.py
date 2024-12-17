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

## AoC 2024 Day 13
### Lucky number 13, wowzers this one is looking tough off the bat. Lock + Load:


from math import gcd

def parse_input(input_text):
    """Parses the input into a list of claw machine configurations."""
    machines = []
    lines = input_text.strip().split("\n")
    for i in range(0, len(lines), 3):
        a_line = lines[i].split()
        b_line = lines[i + 1].split()
        prize_line = lines[i + 2].split()

        a_x, a_y = int(a_line[2][2:-1]), int(a_line[3][2:])
        b_x, b_y = int(b_line[2][2:-1]), int(b_line[3][2:])
        p_x, p_y = int(prize_line[2][2:-1]), int(prize_line[3][2:])

        machines.append(((a_x, a_y), (b_x, b_y), (p_x, p_y)))
    return machines

def diophantine(a, b, c):
    """Solves the Diophantine equation ax + by = c for integers x, y.
    Returns (x, y) if a solution exists, otherwise None."""
    def extended_gcd(x, y):
        if y == 0:
            return x, 1, 0
        g, u, v = extended_gcd(y, x % y)
        return g, v, u - (x // y) * v

    g, x0, y0 = extended_gcd(a, b)
    if c % g != 0:
        return None

    factor = c // g
    return x0 * factor, y0 * factor, g

def find_minimum_tokens(a_x, a_y, b_x, b_y, p_x, p_y):
    """Finds the minimum tokens to align the claw to the prize."""
    # Solve Diophantine equations for X and Y axes
    result_x = diophantine(a_x, b_x, p_x)
    result_y = diophantine(a_y, b_y, p_y)

    if not result_x or not result_y:
        return float('inf')  # No solution exists

    x0, _, gcd_x = result_x
    y0, _, gcd_y = result_y

    # Adjust solution to align gcd scaling
    for n in range(0, 101):
        for m in range(0, 101):
            if (a_x * n + b_x * m == p_x) and (a_y * n + b_y * m == p_y):
                cost = 3 * n + 1 * m
                return cost
    return float('inf')

def solve_claw_machines(input_text):
    machines = parse_input(input_text)
    total_cost = 0
    total_prizes = 0

    for a, b, prize in machines:
        a_x, a_y = a
        b_x, b_y = b
        p_x, p_y = prize

        cost = find_minimum_tokens(a_x, a_y, b_x, b_y, p_x, p_y)
        if cost != float('inf'):
            total_cost += cost
            total_prizes += 1

    return total_prizes, total_cost

# Puzzle input
input_text = """

""" 

total_prizes, total_cost = solve_claw_machines(input_text)
print(f"Total Prizes Won: {total_prizes}")
print(f"Minimum Tokens Needed: {total_cost}")


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
