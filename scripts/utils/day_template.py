import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, logger, _877_cache_now
from utils import support
from datetime import datetime

#Set day/year global variables
DAY:int = 1 #datetime.now().day
YEAR:int = 2023 #datetime.now().year

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow
    #call J.... G.... WENTWORTH. 
    _877_cache_now() #Lol. I blame myself
    #Pull puzzle description and testdata
    testdata = support.pull_puzzle(DAY, YEAR, 1)
    #TODO - Write solution functions for testdata and full data input
    testcase = "duh"
    assert(testcase == "duh")
    global data
    data = support.pull_inputdata(DAY, YEAR)
    return "duh"

@log_time
def part_B():
    logger.info("Solving part B")
    #Check cache status
    _877_cache_now()
    #Pull puzzle description and testdata
    testdata = support.pull_puzzle(DAY, YEAR, 2)
    #TODO - Write solution functions for testdata and full data input
    testcase = "duh"
    assert(testcase == "duh")
    global data
    logger.info(f"length of full dataset-> {len(data)}")
    return "duh"

def main():
    #Solve part A
    resultA = part_A()
    logger.info(f"part A solution: \n{resultA}\n")
    # support.submit_answer(DAY, YEAR, 1, resultA)

    #Solve part B
    resultB = part_B()
    logger.info(f"part B solution: \n{resultB}\n")
    # support.submit_answer(DAY, YEAR, 2, resultB)

    #Recurse lines of code
    LOC = support.recurse_dir(f'./scripts/day{DAY}/')
    logger.info(f"Lines of code \n{LOC}")

    #Delete the cache after submission
    _877_cache_now(".cache", False)
    
if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes
