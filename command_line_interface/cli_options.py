from typing import Optional
from abc import ABC, abstractmethod


class CLIOption(ABC):
    """Abstract Class for an option that a user can select in a shell"""

    @abstractmethod
    def get_option_text(self) -> str:
        """
        Returns the displayed text for this option
        :return: the text for this option
        :rtype: str
        """
        pass

    @abstractmethod
    def perform_option_action(self, quit_menu_after_action=False):
        """
        Preforms the action of this option
        """
        pass

    @abstractmethod
    def should_quit_menu(self):
        pass


class CLIMenuNavigationOption(CLIOption):
    """CLI (Command Line Interface) Option for navigating to another CLI menu"""

    def __init__(self, option_text, cli_menu_dst=None, quit_menu_flag=False):
        """
        :param str option_text: text displayed for this option
        :param Optional[CommandLineInterfaceMenu] cli_menu_dst: menu to navigate to; if None it quits
        :param bool quit_menu_flag: flag to determine whether menu should be quit
        """
        self.option_text = option_text
        self.cli_menu_dst = cli_menu_dst
        self.quit_menu_flag = quit_menu_flag

    def get_option_text(self) -> str:
        return self.option_text

    def perform_option_action(self, quit_menu_after_action=False):
        if self.cli_menu_dst is not None:
            self.cli_menu_dst.start_interface()
        self.quit_menu_flag = quit_menu_after_action

    def should_quit_menu(self):
        return self.quit_menu_flag


class CLIPythonFunctionOption(CLIOption):
    """CLI (Command Line Interface) Option for executing a function"""

    def __init__(self, option_text, function, quit_menu_flag=False):
        """
        :param str option_text: text displayed for this option
        :param func function: Python function to run
        :param bool quit_menu_flag: flag to determine whether menu should be quit
        """
        self.option_text = option_text
        self.function = function
        self.quit_menu_flag = quit_menu_flag

    def get_option_text(self) -> str:
        return self.option_text

    def perform_option_action(self, quit_menu_after_action=False):
        self.function()
        self.quit_menu_flag = quit_menu_after_action

    def should_quit_menu(self):
        return self.quit_menu_flag


class CLIQuitMenuOption(CLIOption):
    """CLI (Command Line Interface) option for quiting a CLI Menu"""

    def __init__(self, option_text):
        """
        :param str option_text: text displayed for this option
        :param bool quit_menu_flag: flag to determine whether menu should be quit
        """
        self.option_text = option_text
        self.quit_menu_flag = True

    def get_option_text(self) -> str:
        return self.option_text

    def perform_option_action(self, quit_menu_after_action=True):
        self.quit_menu_flag = True

    def should_quit_menu(self):
        return self.quit_menu_flag
