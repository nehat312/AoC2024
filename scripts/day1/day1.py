import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, recurse_dir, console
from utils import support
from pathlib import Path, PurePath
from datetime import datetime


@log_time
def process_input(textdata:str, split:bool=True)->list:
    if split:
        data = textdata
        arr = [x.strip() if x != "" else "" for x in data]
    else:
        arr = [x.strip() if x != "" else "" for x in textdata]
    return arr

@log_time
def part_A(YEAR:int, DAY:int):
    input = support.pull_inputdata(YEAR, DAY, 1)
    data = process_input(input, True)
    logger.info("Test data processed/loaded")

@log_time
def part_B(YEAR:int, DAY:int):
    input = support.pull_inputdata(YEAR, DAY, 2)
    data = process_input(input)
    logger.info("test data processed/loaded")

def main():
    #Set day variable
    DAY = 1
    YEAR = 2023 #datetime.now().year
    root_folder = Path.cwd()
    current_date = datetime.now().strftime("%m-%d-%YT%H:%M:%S")
    log_path = PurePath(root_folder, Path(f"./scripts/day{DAY}/_{current_date}.log"))
    fp = PurePath(root_folder, Path(f"./scripts/day{DAY}/test_data.txt"))
    
    global logger
    logger = support.get_logger(log_path, console)
    resultA = part_A(YEAR, DAY)
    
    logger.info(f"Part A solution: \n{resultA}\n")
    resultB = part_B(YEAR, DAY)
    logger.info(f"Part B solution: \n{resultB}\n")

    logger.info(f"Lines of code \n{recurse_dir(f'./scripts/day{DAY}')}")


if __name__ == "__main__":
    main()


########################################################
#Notes
#Part A Notes
