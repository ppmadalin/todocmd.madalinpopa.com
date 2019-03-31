# display.py
""" Module which hold the display functions """
import os
from src.command import Command
from src.exception import InvalidOption


def header():
    """
    defines the header
    :return:
    """
    # header
    title = "TO-DO App"
    print('+' * 50)
    print(f'{"+"}{title:^48}{"+"}')
    print('+' * 50)


def generate_menu(menus):
    """
    defines the main header
    :return:
    """
    print(f'+ {"+":>48s}')
    for key, value in menus.items():
        menu = ''.join(str(key)) + '. ' + value
        length = len(menu) + 5
        print(f'+ {menu:>{length}} {"+":>{47 - length}}')
    print(f'+ {"+":>48s}')
    print(f'+ {"+":+>48s}')


def get_input():
    """
    get the user input
    :return: None
    """
    user_input = input("Chose an action >>> ")
    if not user_input.isdigit():
        raise InvalidOption('Please select a valid menu option')
    if int(user_input) > len(Command.supported_commands):
        message = f'You have available only {len(Command.supported_commands)}'
        raise InvalidOption(message)
    prompt()
    return int(user_input)


def prompt():
    os.system('cls' if os.name == 'nt' else 'clear')
    header()
    generate_menu(Command.supported_commands)


def task_header():
    """ Display the task heaser """
    print(f'{"No.":<5}{"Task":<30}{"Start":<30}{"Due":<30}{"Status":<30}')
    print(f'{"=":=<5}{"=":=<30}{"=":=<30}{"=":=<30}{"=":=<30}')


def display_tasks(task_list):
    """ Display the task list """
    for nr, task in enumerate(task_list):
        name = task.name
        start = task.start_date
        due = task.end_date
        status = task.status
        print(f'{nr:<3}{name:<30}{start:<30}{due:<30}{status:<30}')


if __name__ == '__main__':
    task_header()
