import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, logger, console, _877_cache_now
from utils import support
from datetime import datetime
from itertools import chain
from collections import deque

#Global vars

#Set day/year global variables
DAY:int = 10 #datetime.now().day
YEAR:int = 2023 #datetime.now().year
MOVE_DICT = {
    "|":["N","S"],
    "-":["E","W"],
    "L":["N","E"],
    "J":["N","W"],
    "7":["S","W"],
    "F":["S","E"],
    ".":[""],
    "S":[""]
}
REV_DICT = {
    "N":"S",
    "S":"N",
    "E":"W",
    "W":"E",
}
DIR_DICT = {
    "N":"^",
    "S":"v",
    "E":">",
    "W":"<",
}

def problemsolver(arr:list, part:int) -> int:
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
        
    def scan_start_block(directions:list):
        #Determine start shape by looking at surrounding connections
        start_shape = []
        for direction in directions:
            row, col = cur_pos[0] + direction[0], cur_pos[1] + direction[1]
            if onboard(row, col):
                #Is the opposite of the move we're making...  in the next cells possibles?
                move = REV_DICT[dir_traveled(row, col, cur_pos)]
                #Does that next cell have a connecting pipe
                possibles = MOVE_DICT[arr[row][col]]
                if move in possibles:
                    start_shape.append(REV_DICT[move])
        
        for key, vals in MOVE_DICT.items():
            if start_shape == vals:
                return key

    def pipe_connects(row:int, col:int, cur_pos:tuple, direct:str) -> bool:
        #Grab the reverse of the direction we're moving.  
        revmove = REV_DICT[direct]
        #See if its that direction is in that next cell
        nex_pos_dirs = MOVE_DICT[arr[row][col]]
        #Get the directions of the current position
        cur_dirs = MOVE_DICT[arr[cur_pos[0]][cur_pos[1]]]
        if (direct in cur_dirs) & (revmove in nex_pos_dirs):
            return True
        else:
            return False

    def print_path_taken(pathtaken:list):
        temparr = ["".join("." for y in range(len(arr[0]))) for x in range(len(arr))]
        pathpile = deque(pathtaken)
        while pathpile:
            cp, direct = pathpile.popleft()
            row = cp[0]
            col = cp[1]
            temparr[row] = temparr[row][:col] + direct + temparr[row][col+1:]
        console.log(temparr)

    def chi_town_loop(pathtaken):
        #idea.  For each location in the grid. 
        #Check if it has a path on all 4 sides. 
            #(But check from the perimeter looking in)  Not from the point looking out
        #If it has all 4, maybe its in the loop?
        #Kinda like the tree canopy problem from a few years ago
        #howto
            #Generate all grid point combinations.
            #set intersect the path locations out
            #Check each of the rest for if it has path vars in each direction?
        length = len(arr) 
        width = len(arr[0])

        def pathalldir(point:tuple, pathpoints:list, arr:list):
            for direction in DIR_DICT.keys():
                if direction == "N":
                    points_in_range = [(x, point[1]) for x in range(0, point[0])]
                elif direction == "S":
                    points_in_range = [(x, point[1]) for x in range(point[0], length)]
                elif direction == "E":
                    points_in_range = [(point[0], x) for x in range(point[1], width)]
                elif direction == "W":
                    points_in_range = [(point[0], x) for x in range(0, point[1])]

                if set(points_in_range) & set(pathpoints):
                    continue
                else:
                    return False
            return True
        allpoints = [[(x, y) for y in range(len(arr[0]))] for x in range(len(arr))]
        allpoints = list(chain(*allpoints))
        pathpoints = list(map(lambda x:x[0], pathtaken))
        points_minus_path = set(allpoints).difference(pathpoints)
        pointpile = deque(points_minus_path)
        res = []
        while pointpile:
            point = pointpile.popleft()
            #If a point has pathpoint in every direction, add it to the list
            if pathalldir(point, pathpoints, arr):
                res.append(point)
        return res
      
    #Find the start position
    searchforstart = [[(row, col) for col in range(len(arr[0])) if arr[row][col] == "S"] for row in range(len(arr))]
    start = cur_pos = list(chain(*searchforstart))[0]
    steps = 0
    last_p, pathtaken = "", [(start, "S")]
    directions = [(1,0), (-1,0), (0, 1), (0,-1)]
    start_block = scan_start_block(directions)
    MOVE_DICT["S"] = MOVE_DICT[start_block]
    # [logger.info(f"{key}:{val}") for key, val in MOVE_DICT.items()]
    stopcount = False
    while not stopcount:
        #Only move in directions N,S,E,W respectively
        for direction in directions:
            row, col = cur_pos[0] + direction[0], cur_pos[1] + direction[1]
            #If the next point is on the board, proceed
            if onboard(row, col):
                went = dir_traveled(row, col, cur_pos)
                #If the next point isn't a dot and its not the last point
                if (arr[row][col] != ".") & (last_p != (row, col)):
                    #Check if the pipe connects
                    if pipe_connects(row, col, cur_pos, went):
                        last_p = cur_pos
                        cur_pos = (row, col)
                        steps += 1
                        if part == 2:
                            if not (row, col) == start:
                                pathtaken.append((cur_pos, DIR_DICT[went]))
                        # logger.info(f"went {went} from:{last_p} to {cur_pos} -> stepcount:{steps} ")
                        #Check if its the start
                        if (row, col) == start:
                            stopcount = True

    logger.info(f"Final stepcount:{steps}")

    if part == 1:
        return steps // 2
    if part == 2:
        #Call how many in the loop function
        print_path_taken(pathtaken)
        innerblocks = chi_town_loop(pathtaken)
        if innerblocks:
            return sum(innerblocks)
        else:
            raise ValueError("Something broke~!!!")
@log_time
def part_A():
    logger.info("Solving part 1")
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
    assert testcase == 8, "Test case failed"
    logger.info("Test case passed for part 1")
    #Solve puzzle with full dataset
    # [console.log(f"{idx}:{row}") for idx, row in enumerate(data)]
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
    assert testcase == 10, "Test case failed"
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

#Path finding algos!!!  But now we're chasing animals through the pipes. 
#Reminds me of chicago. Super!  There is one main loop in the maze
#We need to discover how many steps it takes to get from start to finish.  
#Start is defined by S Finish is when the two paths have the same end pt.
#Use a dict for directions in the pipe. 
#1. Check if the next move is on the board
#2. Check if its anything other than a .
#3. Check its able to go direction you of available paths
#4. Check if its at the start (end condition)
#5. If not, iterate steps and continue
#6. Make sures it not where we just came from
#Could count total steps until back at start and divide by 2??  Simple but would work

#Part B Notes

#We suspect there is a nest within the pipe maze they may be hiding in.  Our job now
#is to count the spaces that are contained within the traversal path.  How the hell
#Options
    #1. Could widen the area of the grid and make up a function to test if its part of the loop
    #2. Make a func that can scan for the nearest period in every direction? 
