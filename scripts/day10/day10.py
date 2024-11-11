import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, logger, console, _877_cache_now
from utils import support
from datetime import datetime

#Set day/year global variables
DAY:int = 10 #datetime.now().day
YEAR:int = 2023 #datetime.now().year

    
def problemsolver(arr:list):
    def onboard(x:int, y:int)->bool:
        height, width  = len(arr), len(arr[0])
        if (x < 0) | (x > height):
            return False
        elif (y < 0) | (y > width):
            return False
        else:
            return True
        
    def dir_traveled(x:int, y:int, cur_pos:int)->str:
        if x != cur_pos[0]:
            if x < cur_pos[0]:
                return "W"
            elif x > cur_pos[0]:
                return "E"
        elif x != cur_pos[1]:
            if y < cur_pos[1]:
                return "S"
            elif y > cur_pos[1]:
                return "N"
        else:
            raise ValueError("Soooooomething's screwed up")
        
    def connect_pipe(row:int, col:int, cur_pos:tuple):
        direction = dir_traveled(row, col, cur_pos)
        nextpos = move_dict[arr[row][col]]
        if direction in nextpos:
            return True
        else:
            return False

    move_dict = {
        "|":["N","S"],
        "-":["E","W"],
        "L":["N","E"],
        "J":["N","W"],
        "7":["S","W"],
        "F":["S","E"],
        ".":"",
        "S":"start"
    }
    rev_dict = {
        "N":"S",
        "S":"N",
        "E":"W",
        "W":"E"
    }
    start, steps = (2,0), 0
    #Could count total steps until back at start and divide by 2.  Simple but would work
    cur_pos = start.copy()
    for row in range(start[0] - 1, start[0] + 1):
        for col in range(start[1] - 1, start[1] + 1):
            if onboard(row, col) & (arr[row][col] != ".") & connect_pipe(row, col, cur_pos):
                if (row, col) == start:
                    return steps
                else:
                    steps += 1

    #1. Check if the next move is on the board
    #2. Check if its anything other than a .
    #3. Check its able to go direction you of available paths
    #4. Check if its at the start (end condition)
    #5. If not, iterate steps and continue
    
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
    testcase = problemsolver(testdata)
    #Assert testcase
    assert testcase == 8
    #Solve puzzle with full dataset
    answerA = "" #problemsolver(data)
    return answerA

@log_time
def part_B():
    logger.info("Solving part B")
    #Check cache status
    _877_cache_now()
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2)
    # console.log(f"{tellstory}")
    #Solve puzzle w/testcase
    testcase = "" #problemsolver(testdata)
    #Assert testcase
    assert testcase == ""
    #Solve puzzle with full dataset
    answerB = "" #problemsolver(data)
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

#Path finding algos!!!  But now we're chasing animals through the pipes. 
#Reminds me of chicago. Super!  There is one main loop in the maze
#We need to discover how many steps it takes to get from start to finish.  
#Start is defined by S Finish is when the two paths have the same end pt.
#Use a dict for directions in the pipe. 
#Will need a way to scan a 1 grid border