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
    logger.info("Solving part A")
    #Check cache status J.... G.... WENTWORTH. 
    support._877_cache_now() 
    #Pull puzzle description and testdata
    puzzletext, testdata = support.pull_puzzle(DAY, YEAR, 1, logger)
    #Print the puzzle description to the terminal
    console.log(f"\n{puzzletext}")
    #print the testdata
    testdata = support.process_input(testdata)
    [logger.warning(f"{td}") for td in testdata]
    #TODO - Call solution functions for testcase
    testcase = "duh"
    #Assert the testcase is correct
    assert(testcase == "duh")
    input = support.pull_inputdata(DAY, YEAR, logger)
    #Make data a global for part B which will need it.  (easier than passing it)
    global data
    data = support.process_input(input) #Include False to not split
    #TODO - Call solution functions for fulldatainput
    return "duh"

@log_time
def part_B():
    logger.info("Solving part B")
    #Check cache status
    support._877_cache_now()
    #Pull puzzle description and testdata
    puzzletext, testdata = support.pull_puzzle(DAY, YEAR, 2, logger)
    #Print the puzzle description to the terminal
    console.log(f"\n{puzzletext}")
    #print the testdata
    testdata = support.process_input(testdata)
    [logger.warning(f"{td}") for td in testdata]
    #TODO - Call solution functions for testcase
    testcase = "duh"
    #Assert the testcase is correct
    assert(testcase == "duh")
    global data
    logger.info(f"length of data {len(data)}")
    #TODO - Call solution functions for fulldatainput
    return "duh"

def main():
    #Solve part A
    resultA = part_A()
    logger.info(f"Part A solution: \n{resultA}\n")
    # support.submit_answer(DAY, YEAR, 1, resultA)

    #Solve part B
    resultB = part_B()
    logger.info(f"Part B solution: \n{resultB}\n")
    # support.submit_answer(DAY, YEAR, 2, resultB)

    #Recurse lines of code
    LOC = support.recurse_dir(f'./scripts/day{DAY}/')
    logger.info(f"Lines of code \n{LOC}")

    #Delete the cache after submission
    support._877_cache_now(".cache", True)
    
if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes
