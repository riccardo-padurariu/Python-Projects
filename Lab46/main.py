from domain import PackageList, Package
from command_line_menu import activate_command_line_menu
from menu import display_menu
import sys

def load_package_list(packages):
    with open("default_package_list.txt","r") as file:
        raw_data = file.read()
        raw_data = raw_data.split("\n")
        result = []
        for data in raw_data:
            tokens = data.split(",")
            package = Package(tokens[0].strip(), tokens[1].strip(), tokens[2].strip(), int(tokens[3].strip()), tokens[4].strip())
            result.append(package)
        packages.set_package_list(result)
        file.close()


if __name__ == "__main__":
    package_list = PackageList()
    load_package_list(package_list)
    arguments = sys.argv
    if len(arguments) < 2:
        display_menu(package_list)
    elif arguments[1] == "-c":
        activate_command_line_menu(package_list)
    else:
        print(f"The term {arguments[1]} is not recognized")
