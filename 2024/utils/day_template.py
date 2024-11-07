import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time
from utils.loc import recurse_dir

DAY = './day/'
def data_load(filen:str)->list:
	with open(f'{DAY}{filen}.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [x.strip() if x != "" else "" for x in data]
	return arr

def main():
	@log_time
	def part_A():
		data = data_load()

	@log_time
	def part_B():
		data = data_load()
		
	print(f"Part A solution: \n{part_A()}\n")
	print(f"Part B solution: \n{part_B()}\n")
	print(f"Lines of code \n{recurse_dir(DAY)}")

if __name__ == "__main__":
	main()


########################################################
#Notes
#Part A Notes
