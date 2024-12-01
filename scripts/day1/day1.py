import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, logger, console, _877_cache_now
from utils import support
from datetime import datetime
from collections import Counter

#Set day/year global variables
DAY:int = datetime.now().day
YEAR:int = datetime.now().year

def problemsolver(arr:list, part:int):
    left, right, diffs = [], [], []
    #Transform input strings to two lists
    for row in arr:
        l, r = row.split()
        left.append(int(l))
        right.append(int(r))

    #Sort the lists
    left = sorted(left)
    right = sorted(right)

    if part == 1:
        #Find their differences
        for l, r in zip(left, right):
            diffs.append(abs(l - r))
    
    if part == 2:
        res = Counter(right)
        for val in left:
            if val in right:
                diffs.append(val * res[val])

    return sum(diffs)

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow
    #call J.... G.... WENTWORTH. 
    _877_cache_now() #Lol. I blame myself
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 1)
    # console.log(f"{tellstory}")
    # [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problemsolver(testdata, 1)
    #Assert testcase
    assert testcase == 11, "Test case A failed"
    #Solve puzzle with full dataset
    answerA = problemsolver(data, 1)
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
    testcase = problemsolver(testdata, 2)
    #Assert testcase
    assert testcase == 31, "Test case B failed"
    #Solve puzzle with full dataset
    answerB = problemsolver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)

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
#The theme this year is searching for the Chief Historian!  Everyday will be a
#new location where we will try to find their location before Xmas!  They were sent out
#on expedition to scout historical sites and they've gone missing!  
#
#Starting with an empty list, The search will start at the chief historians office. He's not there
#But they did find lists of where they were going to go for the year.   As the historians 
#split into two groups, each groups tries to reconcile a list of location id's of where
#the chief historian might have gone.  
#
#Initially the two lists are very disimilar.  
# 
# 1. We'll first sort each list from smallest to largest
# 2. for each pair, what is their difference. 
# 3. Add up the list of differences.  Easy peasy

#Part B
#For each value in the left list, if it exists in the right list, 
#Add the value multipled by its number of occurances to the diffs. 
#sum the diffs

#Fun start! 