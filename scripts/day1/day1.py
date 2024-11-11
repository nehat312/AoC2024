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

def extract_calibration(data:list)->list:
    calibrations = []
    for line in data:
        #Check if each character in a line is numeric. 
        #if so add to temp list as a tuple of (number, pos)
        temp = []
        [temp.append((ch, idx)) for idx, ch in enumerate(line) if ch.isdigit()]
            
        #sort the list
        sortme = sorted(temp, key=lambda x:x[1])
        #Take the first and last as your numbers
        calibrations.append(int(f'{sortme[0][0]}{sortme[-1][0]}'))
    return calibrations

def find_all(key:str, line:str):
    idx = line.find(key)
    while idx != -1:
        yield idx
        idx = line.find(key, idx+1)

def extract_updated(data:list)->list:
    calibrations = []
    num_dict = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5, 
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }
    for line in data:
        temp = []
        #Iterate the num_dict keys to see if they exist in each line
        for key in num_dict.keys():
            if key in line:
                #Now find all occurances of each key and add them as a tuple to the temp list
                [temp.append((num_dict[line[x:x+len(key)]], x)) for x in find_all(key, line)]

        #iterate each character in the line to check for numerics
        #Add the number and its index as a tuple
        #Sort the tuples.  Take the first and last
        [temp.append((int(ch), idx)) for idx, ch in enumerate(line) if ch.isdigit()]
        sortme = sorted(temp, key=lambda x:x[1])
        calibrations.append(int(f"{sortme[0][0]}{sortme[-1][0]}"))
    return calibrations

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow
    #call J.... G.... WENTWORTH. 
    _877_cache_now() #Lol. I blame myself
    #Pull puzzle description and testdata
    testdata = support.pull_puzzle(DAY, YEAR, 1)
    calibrations = extract_calibration(testdata)
    assert sum(calibrations) == 142
    calibrations = extract_calibration(data)
    return sum(calibrations)

@log_time
def part_B():
    logger.info("Solving part B")
    #Check cache status
    _877_cache_now()
    #Pull puzzle description and testdata
    testdata = support.pull_puzzle(DAY, YEAR, 2)
    calibrations = extract_updated(testdata)
    assert sum(calibrations) == 281
    calibrations = extract_updated(data)
    logger.info(f"length of full dataset-> {len(data)}")
    return sum(calibrations)

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
