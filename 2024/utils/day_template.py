import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time
from utils.loc import recurse_dir
from utils import support
from pathlib import Path, PurePath
from rich.console import Console
from datetime import datetime


def data_load(DAY:str, filen:str)->list:
    with open(f'{DAY}{filen}.txt', 'r') as f:
        data = f.read().splitlines()
        arr = [x.strip() if x != "" else "" for x in data]
    return arr

@log_time
def part_A(DAY):
    data = data_load(DAY)


@log_time
def part_B(DAY):
    data = data_load(DAY)

def main():
    DAY = './day1/'
    current_date = datetime.now().strftime("%m-%d-%YT%H:%M:%S")
    log_path = PurePath(Path.cwd(), Path(f"./{DAY}/{current_date}.log"))
    fp = PurePath(Path.cwd(), Path(f"./data/{DAY}/day.txt"))
    #Logger setup
    global logger, console
    console = Console()
    logger = support.get_logger(log_path, console)		
    logger.info(f"Part A solution: \n{part_A(DAY)}\n")
    logger.info(f"Part B solution: \n{part_B(DAY)}\n")
    logger.info(f"Lines of code \n{recurse_dir(DAY)}")

if __name__ == "__main__":
    main()


########################################################
#Notes
#Part A Notes
