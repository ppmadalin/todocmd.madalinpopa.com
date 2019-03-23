# todocmd.py
# the main file with the entry point
from src import display
from pathlib import Path
import logging

# configure the logging module
logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

# parent of the todocmd.py (src)
HERE = Path(__file__).parent

# path of the data folder where will be the tasks.csv
data_dir = HERE.joinpath('data')
task_file = data_dir.joinpath('tasks.csv')


# STEP 1: set the path of the tasks.csv files
task_file = Path('tasks.csv')


def main():
    # display.prompt()
    print(HERE)
    print(data_dir)
    print(task_file)

if __name__ == '__main__':
    main()
