import time
import os
import logging
import datetime
import numpy as np
from pathlib import Path
from rich.console import Console
from rich.logging import RichHandler
import requests
import percache
from datetime import timedelta
from bs4 import BeautifulSoup

################################ Global Vars ##############################
AOC_URL = "https://www.adventofcode.com"
with open("./secret/cookie.txt", "r") as f:
    C_is_for_cookie = {"session":f.readline()}

cache = percache.Cache(".cache", livesync=True)
cache.expire = timedelta(seconds=60)

################################ AoC Class ################################

#TODO.  Add an AOC class for functionality sake. 
#Need for testing


################################ data pulling funcs ########################
def _877_cache_now(): #Lol. I couldn't resist
    if os.path.exists(".cache"):
        return True
    else:
        return False
    
@cache
def pull_puzzle(day:int, year:int, part:int, logger:logging):
    logger.info("pulling puzzle data")
    url = f"{AOC_URL}/{year}/day/{day}"
    response = requests.get(url, cookies=C_is_for_cookie, timeout=10)
    
    #Be nice to the servers
    if response.status_code != 200:
        # If there's an error, log it and return no data
        logger.warning(f'Status code: {response.status_code}')
        logger.warning(f'Reason: {response.reason}')
        return None
    else:
        logger.info(f"day {day} data retrieved")

    bs4ob = BeautifulSoup(response.text, features="xml")
    subtext = bs4ob.find_all("article")[part - 1]
    storytime = subtext.get_text()
    sampledata = subtext.select("pre")[0].text
    return storytime, sampledata

@cache
def pull_inputdata(day:int, year:int, logger:logging)->str:
    logger.info("pulling input data")
    url = f"{AOC_URL}/{year}/day/{day}/input"
    response = requests.get(url, cookies=C_is_for_cookie, timeout=10)
    
    #Be nice to the servers
    if response.status_code != 200:
        # If there's an error, log it and return no data
        logger.warning(f'Status code: {response.status_code}')
        logger.warning(f'Reason: {response.reason}')
        return None
    else:
        logger.info(f"day {day} data retrieved")
        return response.text

#TODO - Build function that stores the input data locally in a text file. 
#Hidden in the gitignore, but, have it contain logic that if its
#already downloaded either the puzzle / or input.  To not redownload them
#so as to not hammer Eric's servers.  Wait.  Wouldn't this already be stored
# in your cache? I think that means you'd only pull it once but check

################################# submit funcs ####################################
#TODO - Build these, but go hang out with your fiancee for a while

################################# Timing Funcs ####################################
def log_time(fn):
    def inner(*args, **kwargs):
        tnow = time.time()
        out = fn(*args, **kwargs)
        te = time.time()
        took = te - tnow
        if took <= .000_001:
            logger.info(f"{fn.__name__} ran in {took*1_000_000_000:.3f} ns")
        elif took <= .001:
            logger.info(f"{fn.__name__} ran in {took*1_000_000:.3f} μs")
        elif took <= 1:
            logger.info(f"{fn.__name__} ran in {took*1_000:.3f} ms")
        elif took <= 60:
            logger.info(f"{fn.__name__} ran in {took:.2f} s")
        elif took <= 3600:
            logger.info(f"{fn.__name__} ran in {(took)/60:.2f} m")		
        else:
            logger.info(f"{fn.__name__} ran in {(took)/3600:.2f} h")
        return out
    return inner

################################# Code Line Counter ####################################
def recurse_dir(dir:str = './'):
    """Given the particular days directory, Recurse through and calculate how many lines of code that are uncommented were written for every py file found.

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
                    if (not line.strip().startswith('#')) and (not line.strip() == ''):
                        count += 1

    return count

#############################  Data Transform Funcs  ############################
def process_input(textdata:str, split:bool=True)->list:
    if split:
        data = textdata.splitlines()
        arr = [x.strip() if x != "" else "" for x in data]
    else:
        arr = [x.strip() if x != "" else "" for x in textdata]
    return arr


def date_convert(str_time:str)->datetime:
    """When Loading the historical data.  Turn all the published dates into datetime objects so they can be sorted in the save routine. 

    Args:
        str_time (str): Converts a string to a datetime object 

    Returns:
        dateOb (datetime): str_time as a datetime object
    """    
    dateOb = datetime.datetime.strptime(str_time,'%m-%d-%Y-%H-%M-%S')
    dateOb = np.datetime64(dateOb, "s")
    return dateOb

################################# Logging Funcs ####################################

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

def get_logger(console:Console)->logging.Logger: #log_dir:Path, 
    """Loads logger instance.  When given a path and access to the terminal output.  The logger will save a log of all records, as well as print it out to your terminal. Propogate set to False assigns all captured log messages to both handlers.

    Args:
        log_dir (Path): Path you want the logs saved
        console (Console): Reference to your terminal

    Returns:
        logger: Returns custom logger object.  Info level reporting with a file handler and rich handler to properly terminal print
    """	
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # logger.addHandler(get_file_handler(log_dir)) 
    logger.addHandler(get_rich_handler(console))  
    logger.propagate = False
    return logger

################################# Global Vars (Part deux) ##############################
#Still don't know why I can't load the logger function up above
console = Console()
logger = get_logger(console)

