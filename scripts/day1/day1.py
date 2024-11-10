import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, logger, console
from utils import support
from datetime import datetime


@log_time
def part_A(DAY:int, YEAR:int):
    puzzletext, data = support.pull_puzzle(DAY, YEAR, 1, logger)
    console.log(f"\n{puzzletext}")
    data = support.process_input(data)
    # input = support.pull_inputdata(DAY, YEAR, logger)
    # data = process_input(input) #Include False to not split
    return "duh", data

@log_time
def part_B(DAY:int, YEAR:int, test_data):
    #Solve part B
    console.log(f"\n{support.pull_puzzle(DAY, YEAR, 2, logger)}")
    data = test_data
    return None

def main():
    #Set day variable
    #TODO - make global vars
    DAY = 1 #datetime.now().day
    YEAR = 2023 #datetime.now().year
    
    #Solve part A
    resultA, test_data = part_A(DAY, YEAR)
    logger.info(f"Part A solution: \n{resultA}\n")
    
    #Solve part B
    resultB = part_B(DAY, YEAR, test_data)
    logger.info(f"Part B solution: \n{resultB}\n")
    
    #Recurse lines of code
    LOC = support.recurse_dir(f'./scripts/day{DAY}/')
    logger.info(f"Lines of code \n{LOC}")

if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes
