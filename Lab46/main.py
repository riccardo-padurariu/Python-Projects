from command_line_menu import activate_command_line_menu
from menu import display_menu
import sys

if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) < 2:
        display_menu()
    elif arguments[1] == '-c':
        activate_command_line_menu()
    else:
        print(f"The term {arguments[1]} is not recognized")
