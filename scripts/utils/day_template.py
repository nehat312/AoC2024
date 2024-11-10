import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, logger, console
from utils import support
from datetime import datetime

#Set day/year global variables
DAY = 1 #datetime.now().day
YEAR = 2023 #datetime.now().year

@log_time
def part_A():
    cached_dat_check = support._877_cache_now()
    if cached_dat_check:
        logger.info("Cache exists")
    else:
        logger.info("Creating Cache")
    puzzletext, testdata = support.pull_puzzle(DAY, YEAR, 1, logger)
    console.log(f"\n{puzzletext}")
    testdata = support.process_input(testdata)
    [logger.warning(f"{td}") for td in testdata]
    # input = support.pull_inputdata(DAY, YEAR, logger)
    # data = support.process_input(input) #Include False to not split
    return "duh", testdata #switch to data return for runtime

@log_time
def part_B(test_data:list):
    puzzletext, testdata = support.pull_puzzle(DAY, YEAR, 2, logger)
    console.log(f"\n{puzzletext}")
    testdata = support.process_input(testdata)
    [logger.warning(f"{td}") for td in testdata]
    # input = support.pull_inputdata(DAY, YEAR, logger)
    # data = support.process_input(input) #Include False to not split
    return "duh"

def main():
    #Solve part A
    resultA, test_data = part_A()
    logger.info(f"Part A solution: \n{resultA}\n")
    
    #Solve part B
    resultB = part_B(test_data)
    logger.info(f"Part B solution: \n{resultB}\n")
    
    #Recurse lines of code
    LOC = support.recurse_dir(f'./scripts/day{DAY}/')
    logger.info(f"Lines of code \n{LOC}")

if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes
