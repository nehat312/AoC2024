import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, recurse_dir, logger, console
from utils import support
from datetime import datetime

@log_time
def process_input(textdata:str, split:bool=True)->list:
    if split:
        data = textdata.splitlines()
        arr = [x.strip() if x != "" else "" for x in data]
    else:
        arr = [x.strip() if x != "" else "" for x in textdata]
    return arr

@log_time
def part_A(DAY:int, YEAR:int):
    console.log(f"\n\n{support.pull_puzzle(DAY, YEAR, 1, logger)}")
    input = support.pull_inputdata(DAY, YEAR, logger)
    data = process_input(input) #Include False to not split
    logger.info("Test data processed/loaded")
    return "duh", data

@log_time
def part_B(DAY:int, YEAR:int, test_data):
    #Solve part B
    console.log(f"\n\n{support.pull_puzzle(DAY, YEAR, 2, logger)}")
    data = test_data
    logger.info("test data processed/loaded")

def main():
    #Set day variable
    DAY = 1 #datetime.now().day
    YEAR = 2023 #datetime.now().year
    
    #Solve part A
    resultA, test_data = part_A(DAY, YEAR)
    logger.info(f"Part A solution: \n{resultA}\n")
    
    #Solve part B
    resultB = part_B(DAY, YEAR, test_data)
    logger.info(f"Part B solution: \n{resultB}\n")
    
    #Recurse lines of code
    logger.info(f"Lines of code \n{recurse_dir(f'./scripts/day{DAY}/')}")

if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes
