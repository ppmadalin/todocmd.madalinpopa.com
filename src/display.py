# display.py
""" Module which hold the display functions """
import os


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
        menu = ''.join(key) + '. ' + value
        length = len(menu) + 5
        print(f'+ {menu:>{length}} {"+":>{47 - length}}')
    print(f'+ {"+":>48s}')
    print(f'+ {"+":+>48s}')


def get_input():
    """
    get the user input
    :return: None
    """
    user_input = input("Chose an action > ")
    if user_input.isdigit() and int(user_input) <= 5:
        return int(user_input)
    else:
        print("Invalid option")
        os.system('cls' if os.name == 'nt' else 'clear')
        prompt()
        return None


def prompt():
    os.system('cls' if os.name == 'nt' else 'clear')
    header()
    generate_menu({'1': 'Add task',
                   '2': 'Edit task',
                   '3': 'Delete task',
                   '4': 'List all tasks',
                   '5': 'Exit'})
