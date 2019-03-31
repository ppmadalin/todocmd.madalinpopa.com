
# todocmd

## Description

A to-do command line application which adds tasks within a csv file.
All the tasks are saved into the tasks.csv file. If this file doesn't exist, 
it will be created automatically at first run.

![Demo](https://i.imgur.com/OVdgKJ8.png)

## Functions

A user can perform the following actions:

1. Add a new task
2. Update a task
3. Delete a task
4. List all tasks
5. Save/Exit

## Project layout and file description

```
.
├── bin                     # holds some automation bash/bat/ files
│   ├── todocmd.bat         # windwos
│   └── todocmd.sh          # linux
├── src                     # main folder with the source code
│   ├── data                # contains the task.csv file
│   │   └── tasks.csv       # holds the saved tasks
│   ├── log                 # log folder
│   │   └── log.txt         # log text file
│   ├── __init__.py         # used to mark this folder as package
│   ├── command.py          # contains all the supported commands
│   ├── display.py          # contains all functions for display text
│   ├── exception.py        # contains two exceptions for user bad input
│   ├── task.py             # contains task object
│   └── todocmd.py          # main file. Here is the entry point.
├── tests                   # holds test files
│   ├── __init__.py         # mark folder as package
│   ├── pytest.ini          # pytest configuration file
│   ├── test_display.py     # used to test functions from display.py
│   ├── test_task.py        # used to test task.py
│   └── test_todocmd.py     # used to test command.py
├── LICENSE                 # license file
├── MANIFEST.in             # used to include additional files into pack
├── Pipfile                 # holds the app's dependencies
├── Pipfile.lock            # pipfile
├── README.md               # this file
├── app.log                 # log file for debugging
└── setup.py                # for packing and distributing
```
