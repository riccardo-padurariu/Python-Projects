from domain import PackageList
from tests import test_valid_date, test_delete_destination, test_exists_destination, test_count_days, test_contains
from crud_ui import add_package, modify_package, delete_package
from search_packages_ui import search_package
from package_reports_ui import generate_reports
from filter_package_ui import filter_packages

def undo_operation(package_list):
    """
    The main function for the undo functionality
    :param package_list:
    :return:
    """
    not_empty = package_list.undo_operation()

    if not_empty:
        print("The undo operation was realized successfully!")
    else:
        print("No undo operation can be performed!")


def display_menu():
    """
    The implementation of the main menu
    :return: None
    """
    test_valid_date()
    test_delete_destination()
    test_exists_destination()
    test_count_days()
    test_contains()

    print("---------------------------------")
    print("Welcome to the travel agency app!")
    print("---------------------------------")

    package_list = PackageList()

    while True:
        print("Option 1: Add a tour package")
        print("Option 2: Modify a tour package")
        print("Option 3: Delete tour package")
        print("Option 4: Search for a tour package")
        print("Option 5: Get reports")
        print("Option 6: Filter packages")
        print("Option 7: Undo last operation")
        print("Option 8: Display the current state")
        print("Option 9: Exit application")

        n = input("Enter the desired option: ")
        while not n.isdigit() or (n.isdigit() and (int(n) < 1 or int(n) > 9)):
            n = input("The option must be an integer between 1 and 9. Please enter again: ")
        n = int(n)

        print()

        if n == 1:
            add_package(package_list)
        elif n == 2:
            modify_package(package_list)
        elif n == 3:
            delete_package(package_list)
        elif n == 4:
            search_package(package_list)
        elif n == 5:
            generate_reports(package_list)
        elif n == 6:
            filter_packages(package_list)
        elif n == 7:
            undo_operation(package_list)
        elif n == 8:
            print(package_list)
        elif n == 9:
            print("App closed")
            exit()


        print()