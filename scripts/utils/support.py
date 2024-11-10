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
from typing import Any

################################ Global Vars ##############################
AOC_URL = "https://www.adventofcode.com"
with open("./secret/cookie.txt", "r") as f:
    C_is_for_cookie = {"session":f.readline()}

cache = percache.Cache(".cache", livesync=True)
cache.expire = timedelta(hours=1)

############# ################### AoC Class ################################

#TODO.  Add an AOC class for functionality sake. 
#Need for testing

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
def pull_puzzle(day:int, year:int, part:int):
    """This function pulls down the puzzle description with requests

    Args:
        day (int): Day of AOC
        year (int): Year of AOC
        part (int): Which part is being solved

    Returns:
        _type_: _description_
    """    
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
def pull_inputdata(day:int, year:int)->str:
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

################################# submit funcs ##############################
@cache
def submit_answer(day:int, year:int, part:int, answer:Any=""):
    if not answer:
        logger.warning("No Soup for you!!!! No answer submitted")
        return
    
    logger.info(f"Posting {answer} for part {part}")
    url = f"{AOC_URL}/{year}/day/{day}/answer"
    response = requests.post(
        url = url,
        data = {"level":part, "answer":answer},
        cookies = C_is_for_cookie, 
        timeout = 10
    )
    #Be nice to the servers
    if response.status_code != 200:
        # If there's an error, log it and return no data
        logger.warning(f'Status code: {response.status_code}')
        logger.warning(f'Reason: {response.text}')
        return
    else:
        logger.info(f"AOC day {day} successfully submitted :tada:")
        bs4ob = BeautifulSoup(response.text, "xml")
        console.log(bs4ob.find_all("article")[2].get_text())

#TODO - Will need to come back and check these

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
                    if (not line.strip().startswith('#')) and (not line.strip() == ''):
                        count += 1

    return count

#############################  Data Transform Funcs  ########################
def process_input(textdata:str, split:bool=True)->list:
    if split:
        data = textdata.splitlines()
        arr = [x.strip() if x != "" else "" for x in data]
    else:
        arr = [x.strip() if x != "" else "" for x in textdata]
    return arr


def date_convert(str_time:str)->datetime:
    """
    When Loading the historical data.  Turn all the published dates into
    datetime objects so they can be sorted in the save routine. 

    Args:
        str_time (str): Converts a string to a datetime object 

    Returns:
        dateOb (datetime): str_time as a datetime object
    """    
    dateOb = datetime.datetime.strptime(str_time,'%m-%d-%Y-%H-%M-%S')
    dateOb = np.datetime64(dateOb, "s")
    return dateOb

################################# Logging Funcs #############################

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

################################# Global Vars (Part deux) ##################
#Still don't know why I can't load the logger function up above
console = Console()
logger = get_logger(console)

