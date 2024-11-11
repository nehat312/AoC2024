import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, logger, console, _877_cache_now
from utils import support
from datetime import datetime
from itertools import chain

#Set day/year global variables
DAY:int = 10 #datetime.now().day
YEAR:int = 2023 #datetime.now().year

    
def problemsolver(arr:list) -> int:
    def onboard(x:int, y:int) -> bool:
        height, width  = len(arr), len(arr[0])
        if (x < 0) | (x >= height):
            # logger.warning(f"({x}, {y}) not on board")
            return False
        elif (y < 0) | (y >= width):
            # logger.warning(f"({x}, {y}) not on board")
            return False
        else:
            return True
        
    def dir_traveled(x:int, y:int, cur_pos:tuple)->str:
        if x != cur_pos[0]:
            if x < cur_pos[0]:
                return "N"
            elif x > cur_pos[0]:
                return "S"
        elif y != cur_pos[1]:
            if y < cur_pos[1]:
                return "W"
            elif y > cur_pos[1]:
                return "E"
        else:
            return None
        
    def pipe_connects(row:int, col:int, cur_pos:tuple) -> bool:
        direction = dir_traveled(row, col, cur_pos)
        if isinstance(direction, str):
            cur_pos_dirs = move_dict[arr[cur_pos[0]][cur_pos[1]]]
            if direction in cur_pos_dirs:
                nex_pos_dirs = move_dict[arr[row][col]]
                if (direction == rev_dict[nex_pos_dirs[0]]) | (direction == rev_dict[nex_pos_dirs[1]]):
                    return True
            else:
                return False
        else:
            return False

    move_dict = {
        "|":["N","S"],
        "-":["E","W"],
        "L":["N","E"],
        "J":["N","W"],
        "7":["S","W"],
        "F":["S","E"],
        "S":["N", "S", "E", "W"]
    }
    rev_dict = {
        "N":"S",
        "S":"N",
        "E":"W",
        "W":"E",
    }
    #Find the start position
    searchforstart = [[(row, col) for col in range(len(arr[0])) if arr[row][col] == "S"] for row in range(len(arr))]
    start = cur_pos = list(chain(*searchforstart))[0]
    steps = 0
    last_p = ""
    stopcount = False
    while not stopcount:
        #Only move in directions N,S,E,W respectively
        for direction in [(1,0), (-1,0), (0, 1), (0, -1)]:
            row, col = cur_pos[0] + direction[0], cur_pos[1] + direction[1]
            # If the next point is on the board, proceed
            if onboard(row, col):
                # If the next point isn't a dot and its not the last point
                if (arr[row][col] != ".") & (last_p != (row, col)):
                    #End whileloop condition
                    if (row, col) == start:
                        steps += 1
                        stopcount = True
                        logger.info(f"Final stepcount:{steps}")
                        break
                    else:
                        if pipe_connects(row, col, cur_pos):
                            went = dir_traveled(row, col, cur_pos)
                            last_p = cur_pos
                            cur_pos = (row, col)
                            steps += 1
                            logger.info(f"stepcount:{steps} from:{last_p} to {cur_pos} -> {went}")

                        #Need logic to continue here.  Probably source of bug
    return steps // 2
    #1. Check if the next move is on the board
    #2. Check if its anything other than a .
    #3. Check its able to go direction you of available paths
    #4. Check if its at the start (end condition)
    #5. If not, iterate steps and continue
    #6. Make sures it not where we just came from
    #Could count total steps until back at start and divide by 2??  Simple but would work
    
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
    logger.info("Test case passed for part A")
    #Solve puzzle with full dataset
    answerA = problemsolver(data)
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