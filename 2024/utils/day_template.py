import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time
from utils.loc import recurse_dir
from pathlib import Path, PurePath
from rich.console import Console


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
    log_path = PurePath(Path.cwd(), Path(f"./{DAY}/logs/{current_date}.log"))
    fp = PurePath(Path.cwd(), Path(f"./data/json/{current_date}.json"))
    #Logger setup
    global logger, console
    console = Console()
    logger = support.get_logger(log_path, console)		

    print(f"Part A solution: \n{part_A()}\n")
    print(f"Part B solution: \n{part_B()}\n")
    print(f"Lines of code \n{recurse_dir(DAY)}")

if __name__ == "__main__":
    main()


########################################################
#Notes
#Part A Notes
