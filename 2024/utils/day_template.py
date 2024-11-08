import os
import sys
from utils.time_run import log_time
from utils.loc import recurse_dir
from utils import support
from pathlib import Path, PurePath
from rich.console import Console
from datetime import datetime
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

@log_time
def data_load(fp:str)->list:
    #TODO.  Make sure you have the right file path
    with open(f'{fp}.txt', 'r') as f:
        data = f.read().splitlines()
        arr = [x.strip() if x != "" else "" for x in data]
    return arr

@log_time
def part_A(fp:str):
    data = data_load(fp)
    logger.info("data loaded")

@log_time
def part_B(fp:str):
    data = data_load(fp)
    logger.info("data loaded")

def main():
    #Set day variable
    global DAY
    DAY = 1
    current_date = datetime.now().strftime("%m-%d-%YT%H:%M:%S")
    log_path = PurePath(Path.cwd(), Path(f"./2024/day{DAY}/_{current_date}.log"))
    fp = PurePath(Path.cwd(), Path(f"./2024/day{DAY}.txt"))
    #Logger setup
    global logger, console
    console = Console()
    logger = support.get_logger(log_path, console)
    logger.info(f"Part A solution: \n{part_A(fp)}\n")
    logger.info(f"Part B solution: \n{part_B(fp)}\n")
    logger.info(f"Lines of code \n{recurse_dir(f'./day{DAY}')}")

if __name__ == "__main__":
    main()


########################################################
#Notes
#Part A Notes
