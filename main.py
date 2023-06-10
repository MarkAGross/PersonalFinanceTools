import argparse
import definitions
from command_line_interface.cli_menu import CLIMenu
from command_line_interface.cli_options import CLIQuitMenuOption


def launch_cli():
    """Starts the Command Line Interface for the application"""
    main_menu = CLIMenu("Personal Finance Tools Interface")
    main_menu.add_option(CLIQuitMenuOption("Quit"))
    main_menu.start_menu()


#####################################
# MAIN METHOD
#####################################
def main():
    """Main function to begin application"""

    # Parse System Arguments
    arg_parser = argparse.ArgumentParser(description=definitions.APP_DESCRIPTION)
    arg_parser.add_argument('--app_mode',
                            type=str,
                            default=definitions.DEFAULT_APP_MODE,
                            help='An optional integer argument')
    args = arg_parser.parse_args()

    # Determining Application Mode and Running
    print(f"Application starting mode: {args.app_mode}\n")
    match args.app_mode:
        case "cli":
            launch_cli()
        case _:
            print(f"Error launching application. Application Mode not recognized: {args.app_mode}")


if __name__ == "__main__":
    main()
