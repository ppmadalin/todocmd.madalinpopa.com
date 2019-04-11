# display.py
""" Module which hold the display functions """
import os
from src.controller.basectrl import BaseController
from src.exception import InvalidOption


class TerminalView:

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def get_input():
        """
        get the user input
        :return: None
        """
        user_input = input("Chose an action >>> ")
        if not user_input.isdigit():
            raise InvalidOption('Please select a valid menu option')
        if int(user_input) > len(BaseController.supported_commands):
            message = f'Available only {len(BaseController.supported_commands)}'
            raise InvalidOption(message)
        TerminalView.prompt()
        return int(user_input)

    @staticmethod
    def prompt():
        os.system('cls' if os.name == 'nt' else 'clear')
        TerminalView.header()
        TerminalView.generate_menu(BaseController.supported_commands)

    @staticmethod
    def task_header():
        """ Display the task heaser """
        print(f'{"No.":<5}{"Task":<30}{"Start":<30}{"Due":<30}{"Status":<30}')
        print(f'{"=":=<5}{"=":=<30}{"=":=<30}{"=":=<30}{"=":=<30}')

    @staticmethod
    def display_tasks(task_list):
        """ Display the task list """
        for nr, task in enumerate(task_list):
            name = task.name
            start = task.start_date
            due = task.end_date
            if task.status == 'True':
                mark = "[x]"
            else:
                mark = "[ ]"
            print(f'{nr:<3}{name:<30}{start:<30}{due:<30}{mark:<30}')
        return True
