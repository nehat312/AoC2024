import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, logger, console, _877_cache_now
from utils import support
from datetime import datetime
from itertools import combinations
from functools import cache as cashish

#Set day/year global variables
DAY:int = 12 #datetime.now().day
YEAR:int = 2023 #datetime.now().year

def problemsolver(arr:list, part:int):
    def find(line:str, ch:int):
        return [x for x, ltr in enumerate(line) if ltr == ch]

    def is_valid(group:list):
        for x in range(len(group)):
            if group[x] + 1 == group[x + 1]:
                pass
    
    @cashish
    def possible_combos(line:str, groups:tuple):
        possibles = []
        groups = tuple(map(int, groups.split(",")))
        unknown = find(line, "?")
        broken = find(line, "#")
        functional = find(line, ".")
        for combo in combinations(unknown, broken):
            logger.info(combo)


    def decode_springs(data:list):
        '''
        . -> operational
        # -> broken
        ? -> unknown
        '''
        counts = []
        for springs in data:
            line, groups = springs.split(" ")
            counts += possible_combos(line, groups)

        return counts
    
    arrangements = decode_springs(arr)

    if part == 1:
        return sum(arrangements)

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow
    #call J.... G.... WENTWORTH. 
    _877_cache_now() #Lol. I blame myself
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 1)
    console.log(f"{tellstory}")
    # console.log(f"Sample data:\n")
    # [console.log(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = ""#problemsolver(testdata, 1)
    #Assert testcase
    assert testcase == 21, "Test case A failed"
    #Solve puzzle with full dataset
    answerA = "" #problemsolver(data, 1)
    return answerA

@log_time
def part_B():
    logger.info("Solving part B")
    #Check cache status
    _877_cache_now()
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2)
    # console.log(f"{tellstory}")
    # [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = "" #problemsolver(testdata, 2)
    #Assert testcase
    assert testcase == "", "Test case B failed"
    #Solve puzzle with full dataset
    answerB = "" #problemsolver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)

    #Solve part A
    resultA = part_A()
    logger.info(f"part A solution: \n{resultA}\n")
    # support.submit_answer(DAY, YEAR, 1, resultA)

    #Solve part B
    # resultB = part_B()
    # logger.info(f"part B solution: \n{resultB}\n")
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

#ooook so we've got rows of springs.  

# . = operational
# # = Damaged
# ? = Unknown
# our map is partially obscured so we don't know the groups are. But we have a list of the 
            # size of contiguous groups of springs that are damaged
            #in order
# Our task:
# We need to count how many different arrangements are possible for each row of data and sum those up.
# We have