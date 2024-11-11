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

# def problemsolver(inputdata:list):
#     pass

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow
    #call J.... G.... WENTWORTH. 
    _877_cache_now() #Lol. I blame myself
    #Pull puzzle description and testdata
    testdata = support.pull_puzzle(DAY, YEAR, 1)
    #Solve puzzle w/testcase
    testcase = "" #problemsolver(testdata)
    #Assert testcase
    assert testcase == ""
    #Solve puzzle with full dataset
    answerA = "Marla" #problemsolver(data)
    return answerA

@log_time
def part_B():
    logger.info("Solving part B")
    #Check cache status
    _877_cache_now()
    #Pull puzzle description and testdata
    testdata = support.pull_puzzle(DAY, YEAR, 2)
    #Solve puzzle w/testcase
    testcase = "" #problemsolver(testdata)
    #Assert testcase
    assert testcase == ""
    #Solve puzzle with full dataset
    answerB = "Hooch\nWhat a hitter! :bat: " #problemsolver(data)
    logger.info(f"length of full dataset-> {len(data)}")
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

#Wow  So.  This is going to require a graph traversal at some point.  But!  we're chasing animals through 
#pipes now.  Super!  There are two main loops throughout the maze.  We need to discover how many
#steps it takes to get from start to finish.  
#Start is defined by S
#Finish is whe the two paths have the same end pt
#Use a dict for directions in the pipe. 
#Will need a way to scan a 1 grid border