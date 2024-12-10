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
## Day7 Attempt(s)... 
def possible_target_form(target, nums):
    if len(nums) == 1:
        return nums[0] == target

    possible_results = {nums[0]}
    for n in nums[1:]:
        new_results = set()
        for val in possible_results:
            add_res = val + n
            if add_res == target:
                return True
            new_results.add(add_res)

            mul_res = val * n
            if mul_res == target:
                return True
            new_results.add(mul_res)

        possible_results = new_results

    return (target in possible_results)

def solve(input_data):
    total = 0
    for line in input_data:
        line = line.strip()
        if not line or ':' not in line:
            continue
        left, right = line.split(':', 1)
        target_str = left.strip()
        nums_str = right.strip()
        if not target_str or not nums_str:
            continue

        target = int(target_str)
        nums = list(map(int, nums_str.split()))

        if possible_target_form(target, nums):
            total += target
    return total

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)

    result = solve(data)
    print(result)





########################################################
#Notes
#PART A Notes
## goal:
##

#PART B Notes
#
#
# %%

# import itertools

# def evaluate_equation(numbers, operators):
#     """
#     Evaluates a list of numbers and operators from left to right.

#     Args:
#       numbers: A list of integers.
#       operators: A list of operators ('+' or '*').

#     Returns:
#       The result of the evaluated equation.
#     """
#     result = numbers[0]
#     for i in range(1, len(numbers)):
#         if operators[i - 1] == '+':
#             result += numbers[i]
#         elif operators[i - 1] == '*':
#             result *= numbers[i]
#     return result

# def find_valid_equations(equations):
#     """
#     Finds the valid equations from a list of equations.

#     Args:
#       equations: A list of strings, where each string is an equation 
#                  in the format "test_value: number1 number2 ..."

#     Returns:
#       A list of valid test values (integers).
#     """
#     valid_test_values = []
#     for equation in equations:
#         test_value, numbers_str = equation.split(':')
#         test_value = int(test_value)
#         numbers = [int(x) for x in numbers_str.strip().split()]

#         # Generate all possible operator combinations
#         operators = itertools.product(['+', '*'], repeat=len(numbers) - 1)
#         for op_combo in operators:
#             if evaluate_equation(numbers, op_combo) == test_value:
#                 valid_test_values.append(test_value)
#                 break  # Move on to the next equation once a valid combo is found

#     return valid_test_values

# if __name__ == "__main__":
#     with open("day7_input.txt", "r") as f:
#         equations = f.readlines()

#     valid_test_values = find_valid_equations(equations)
#     total_calibration_result = sum(valid_test_values)

#     print("Total Calibration Result:", total_calibration_result)