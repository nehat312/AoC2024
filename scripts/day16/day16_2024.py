#%%
import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
#from utils.support import log_time, _877_cache_now, logger, console
#from utils import support
from datetime import datetime
#import numpy as np

#Set day/year global variables
DAY:int = datetime.now().day
YEAR:int = datetime.now().year

########################################################

## AoC 2024 Day 16

### 

#%%
