from typing import Optional
from command_line_interface.cli_options import CLIOption


class CLIMenu:
    """Creates a single menu on a Command Line Interface for users to navigate and execute functionality"""

    def __init__(self, name):
        """
        :param str name: name of this menu
        """
        self.name = name
        self.options = []

    def start_menu(self):
        """Prints the menu options until a valid option is selected by the user"""

        # Option Selected by User
        option_selected = None

        # Build user options prompt
        user_prompt = "Select an option... \n"
        for option in enumerate(self.options):
            option_index = option[0]
            option_name = option[1].get_option_text()
            user_prompt += f"{option_index}) {option_name}\n"
        user_prompt += "\nChoice: "

        # Print CLI Menu Header
        print(f"{self.name.upper()}")
        print("----------------------------------------")

        # Print CLI Options and Get User Input
        while option_selected is None or not option_selected.should_quit_menu():
            user_input = input(user_prompt)
            print()

            # Determine Option Selected
            option_selected = self._get_user_selected_option(user_input=user_input)

        option_selected.perform_option_action()

    def add_option(self, option):
        """
        Adds option to this menu
        :param CLIOption option: option to appear to user
        """
        self.options.append(option)

    def _get_user_selected_option(self, user_input) -> Optional[CLIOption]:
        """Determines the option selected by user in input value
        :param str user_input: input value from user as a str
        :return: CLIOption object if one has been selected; None otherwise
        :rtype: Optional[CLIOption]
        """
        if self._is_valid_user_input(user_input=user_input):
            return self.options[int(user_input)]
        else:
            return None

    def _is_valid_user_input(self, user_input) -> bool:
        """Determines if user input is a valid selection
        :param str user_input: input value from user as a str
        :return: true if input is valid selection from this menu's options, false otherwise
        :rtype: bool
        """
        try:
            user_input_int = int(user_input)
            if 0 <= user_input_int <= (len(self.options) - 1):
                # User input is valid
                return True
            else:
                # User input not within the bounds of the user options
                raise ValueError
        except ValueError:
            print(f"ERROR: Input option must be a number between 0 and "
                  f"{len(self.options)}. Value Selected: {user_input}")
            # User input is invalid
            return False
