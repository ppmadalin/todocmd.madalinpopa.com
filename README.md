
# todocmd

## Description

A to-do command line application which adds tasks within a csv file.
All the tasks are saved into the tasks.csv file. If this file doesn't exist, 
it will be created automatically at first run.

## Functions

A user can perform the following actions:

1. Add a new task
2. Update a task
3. Delete a task
4. List all tasks
5. Save/Exit

## Project layout and file description
.
├── LICENSE               # license file 
├── MANIFEST.in           # used to include additional files into package
├── Pipfile               # holds the app's dependencies
├── Pipfile.lock          # pipfile
├── README.md             # this file
├── app.log               # log file for debugging
├── bin                   # holds some automation bash/bat file
│   ├── todocmd.bat       # windwos
│   └── todocmd.sh        # linux
├── setup.py              # setup.py for for packing and distributing
├── src                   # main folder with the source code
│   ├── __init__.py       # used to mark this folder as package
│   ├── command.py        # contains all the supported commands
│   ├── data              # contains the task.csv file
│   │   └── tasks.csv     # holds the saved tasks
│   ├── display.py        # contains all the logic for display
│   ├── exception.py      # contains two exceptions for bad input
│   ├── log               # log folder
│   │   └── log.txt       # log text file
│   ├── task.py           # contains task object 
│   └── todocmd.py        # main file. Here is the entry point of the program
└── tests                 # holds test files
    ├── __init__.py       # mark folder as package
    ├── pytest.ini        # pytest configuration file
    ├── test_display.py   # used to test the functions from display.py
    ├── test_task.py      # used to test task.py 
    └── test_todocmd.py   # used to test command.py 

