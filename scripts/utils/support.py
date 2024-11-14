import os
import time
import logging
import datetime
import percache
import requests
import numpy as np
from typing import Any
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import timedelta
from rich.console import Console
from rich.logging import RichHandler

################################# Logging Funcs #############################
def get_logger(console:Console)->logging.Logger: #log_dir:Path, 
    """
    Loads logger instance.  When given a path and access to the terminal output.
    The logger will save a log of all records, as well as print it out to your
    terminal. Propogate set to False assigns all captured log messages to both
    handlers.

    Args:
        log_dir (Path): Path you want the logs saved
        console (Console): Reference to your terminal

    Returns:
        logger: Returns custom logger object.  Info level reporting with a file
        handler and rich handler to properly terminal print
    """	
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # logger.addHandler(get_file_handler(log_dir)) 
    logger.addHandler(get_rich_handler(console))  
    logger.propagate = False
    return logger

def get_file_handler(log_dir:Path) -> logging.FileHandler:
    """Assigns the saved file logger format and location to be saved

    Args:
        log_dir (Path): Path to where you want the log saved

    Returns:
        filehandler(handler): This will handle the logger's format and file management
    """	
    LOG_FORMAT = "%(asctime)s|%(levelname)-8s|%(lineno)-3d|%(funcName)-14s|%(message)s|" 
    file_handler = logging.FileHandler(log_dir)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT, "%m-%d-%Y-%H:%M:%S"))
    return file_handler

def get_rich_handler(console:Console) -> RichHandler:
    """Assigns the rich format that prints out to your terminal

    Args:
        console (Console): Reference to your terminal

    Returns:
        rh(RichHandler): This will format your terminal output
    """
    FORMAT_RICH = "%(message)s"
    rh = RichHandler(level=logging.INFO, console=console)
    rh.setFormatter(logging.Formatter(FORMAT_RICH))
    return rh

################################ Global Vars ##############################
AOC_URL = "https://adventofcode.com"
with open("./secret/cookie.txt", "r") as f:
    C_IS_4_COOKIE = {"session":f.readline()}

cache = percache.Cache(".cache", livesync=True)
cache.expire = timedelta(hours=1)
console = Console()
logger = get_logger(console)


################################# Timing Funcs ##############################
def log_time(fn):
    """
    Decorator timing function.  Accepts any function and returns a logging
    statement with the amount of time it took to run. DJ, I use this code
    everywhere still.  Thank you bud!

    Args:
        fn (function): Input function you want to time
    """	
    def inner(*args, **kwargs):
        tnow = time.time()
        out = fn(*args, **kwargs)
        te = time.time()
        took = te - tnow
        if took <= .000_001:
            logger.info(f"{fn.__name__} ran in {took*1_000_000_000:.2f} ns")
        elif took <= .001:
            logger.info(f"{fn.__name__} ran in {took*1_000_000:.2f} μs")
        elif took <= 1:
            logger.info(f"{fn.__name__} ran in {took*1_000:.2f} ms")
        elif took <= 60:
            logger.info(f"{fn.__name__} ran in {took:.2f} s")
        elif took <= 3600:
            logger.info(f"{fn.__name__} ran in {(took)/60:.2f} m")		
        else:
            logger.info(f"{fn.__name__} ran in {(took)/3600:.2f} h")
        return out
    return inner

################################ data pulling/cache managment funcs #########
def _877_cache_now(
        cache_file:str=".cache", 
        del_cache:bool=False, 
        cache_closed:bool=False
    ): 
    """
    First off. I couldn't resist the JG Wentworth shoutout in the function
    naming. Second. This function will iterate through each of the cache files
    verifying each components existence.  You also may include a boolean
    variable of whether or not you want to clear the cache when you call to
    check on it. 

    Args:
        cache_file (str, optional): Cache file in question. Defaults to ".cache".
        del_cache (bool, optional): Do you want to delete the cache?. Defaults to False.
        cache_closed (bool, optional): Has the cache been closed. Defaults to False.
    """
    cache_files = [f"{cache_file}.{cachetype}" for cachetype in ["bak","dat","dir"]]
    for file in cache_files:
        if os.path.exists(file):
            if del_cache:
                cache.close()
                logger.warning(f"cache closed")
                cache_closed = True
                break
            else:
                logger.info(f"cache file exists-> {file}")
        else:
            logger.info(f"creating cache file-> {file}")
    if cache_closed:
        [os.remove(file) for file in cache_files]
        logger.critical("cache cleared")

@cache
def pull_puzzle(day:int, year:int, part:int, tellstory:bool=True)-> str:
    """This function pulls down the puzzle description with requests

    Args:
        day (int): Day of AOC
        year (int): Year of AOC
        part (int): Which part is being solved

    Returns:
        sampledata[str]: The testcase dataset in str form
    """    
    logger.info("pulling puzzle data")
    url = f"{AOC_URL}/{year}/day/{day}"
    response = requests.get(url, cookies=C_IS_4_COOKIE, timeout=10)
    
    #Be nice to the servers
    if response.status_code != 200:
        # If there's an error, log it and return no data
        logger.warning(f'Status code: {response.status_code}')
        logger.warning(f'Reason: {response.reason}')
        return None
    else:
        logger.info(f"day {day} puzzle desc part {part} retrieved")

    bs4ob = BeautifulSoup(response.text, features="xml")
    subtext = bs4ob.find_all("article")[part - 1]
    storytime = subtext.get_text()
    
    if part == 1:
        sampledata = subtext.select("pre")[-2].text
    elif part == 2:
        sampledata = subtext.select("pre")[-2].text

    console.log(f"\n{storytime}")

    #process the sample data
    sampledata = process_input(sampledata, tellstory) #Include extra False to not split

    return storytime, sampledata

@cache
def pull_inputdata(day:int, year:int)->str:
    """This function retrieves the full dataset for evaluation.

    Args:
        day (int): Day of AOC
        year (int): Year of AOC

    Returns:
        response.text (str): the dataset in string form
    """
    logger.info("pulling input data")
    url = f"{AOC_URL}/{year}/day/{day}/input"
    response = requests.get(url, cookies=C_IS_4_COOKIE, timeout=10)
    
    #Be nice to the servers
    if response.status_code != 200:
        # If there's an error, log it and return no data
        logger.warning(f'Status code: {response.status_code}')
        logger.warning(f'Reason: {response.reason}')
        return None
    else:
        logger.info(f"day {day} input data retrieved")
        #Process the data
        data = process_input(response.text, False) #Include extra False to not split
        logger.info(f"Shape of dataset (row,col)-> {len(data), len(data[0])}")
        return data

#############################  Data Transform Funcs  ########################
def process_input(textdata:str, testd:bool, split:bool=True)->list:
    """Function to process input datasets.  Both testcase and full datasets

    Args:
        textdata (str): Usually one huge string of the input data
        split (bool, optional): Whether or not you want to newline split the string. Defaults to True.

    Returns:
        arr (list): List of the dataset
    """    
    if split:
        data = textdata.splitlines()
        arr = [x.strip() if x != "" else "" for x in data]
    else:
        arr = [x.strip() if x != "" else "" for x in textdata]
    if testd:
        console.log("\nSample Data:\n")
        [console.log(f"{td}") for td in arr]
        console.log("\n")
    return arr

################################# submit funcs ##############################
@cache
def submit_answer(day:int, year:int, part:int, answer:Any=""):
    """This cached function will submit your answers for official scoring.

    Args:
        day (int): Day of AOC
        year (int): Year of AOC
        part (int): Which part is being solved
        answer (Any, optional): Answer to part. Defaults to "".
    """
    if not answer:
        logger.critical("No Soup for you!!!! No answer submitted")
        return
    
    logger.warning(f"Posting {answer} for part {part}")
    url = f"{AOC_URL}/{year}/day/{day}/answer"
    response = requests.post(
        url = url,
        data = {"level":part, "answer":answer},
        cookies = C_IS_4_COOKIE, 
        timeout = 10
    )
    #TODO - Keep a configs file that can track when the last posting was and to not post another request within x minutes.  I think he has a minute limit on them but I can't quite remember. 
        #Either way.  Don't hammer his servers. 
    #Be nice to the servers
    if response.status_code != 200:
        # If there's an error, log it and return no data
        logger.warning(f'Status code: {response.status_code}')
        logger.warning(f'Reason: {response.text}')
        return
    else:
        logger.info(f"POST successful for day {day} of {year}")
        logger.info("Determining answer")
        bs4ob = BeautifulSoup(response.text, "xml")
        web_text = bs4ob.body.main.article.get_text()
        possiblygood = ["That's the right answer", "You don't seem to be solving the right level"]
        temp = bs4ob.find_all("p")
        for val in temp:
            if val.text.startswith(possiblygood[0]):
                logger.info("Answer Correct!")
                break
            elif val.text.startswith(possiblygood[1]):
                logger.info("Answer already submitted")
                break

        #If we don't find success.  We warn
        logger.warning(f"{web_text}")

#TODO - Create func that can add rows and / or update a markdown table.   or store it in a dataclass.  I'd like it to be able to add new days and update it as I complete sections.  
    #Make it part of a successful submit function

################################# Code Line Counter #########################
def recurse_dir(dir:str = './'):
    """
    Given the particular days directory, Recurse through and calculate how many
    lines of code that are uncommented were written for every py file found.

    Args:
        dir (str, optional): Directory you want to search. Defaults to './'.

    Returns:
        count (int): Lines of code counted in directory
    """    
    count = 0
    for file in os.listdir(dir):
        if not os.path.isfile(dir + file):
            count += recurse_dir(dir + file + '/')
        elif file.endswith('.py'):
            with open(dir + file, 'r') as f:
                for line in f.readlines():
                    #Don't count any line that starts with # or is empty
                    if (not line.strip().startswith('#')) and (not line.strip() == ''):
                        count += 1

    return count