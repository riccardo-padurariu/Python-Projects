from domain import PackageList
from tests_crud import test_crud
from crud_ui import add_package, modify_package, delete_package
from search_packages_ui import search_package
from package_reports_ui import generate_reports
from filter_package_ui import filter_packages
from tests_domain import test_domain
from tests_filter import test_filter
from tests_reports import test_reports
from tests_search import test_search


def undo_operation(package_list):
    """
    The main function for the undo functionality
    :param package_list: PackageList
    :return: None
    """
    not_empty = package_list.undo_operation()

    if not_empty:
        print("The undo operation was realized successfully!")
    else:
        print("No undo operation can be performed!")

def display_state(package_list):
    """
    Function that displays the current state of the package_list
    :param package_list: PackageList
    :return: None
    """
    print(package_list)

def exit_app(package_list):
    """
    Function that closes the app
    :param package_list: PackageList
    :return: None
    """
    print("App closed")
    exit()

menu = [("Add a tour package", add_package),
        ("Modify a tour package", modify_package),
        ("Delete tour package", delete_package),
        ("Search for a tour package", search_package),
        ("Get reports", generate_reports),
        ("Filter packages", filter_packages),
        ("Undo last operation", undo_operation),
        ("Display the current state", display_state),
        ("Exit application", exit_app)]

def display_menu():
    """
    The implementation of the main menu
    :return: None
    """
    test_crud()
    test_domain()
    test_search()
    test_reports()
    test_filter()

    print("---------------------------------")
    print("Welcome to the travel agency app!")
    print("---------------------------------")

    package_list = PackageList()

    while True:
        for index, func in enumerate(menu): print(f"Option {index+1}: {func[0]}")

        n = input("Enter the desired option: ")
        while not n.isdigit() or (n.isdigit() and (int(n) < 1 or int(n) > len(menu))):
            n = input("The option must be an integer between 1 and 9. Please enter again: ")
        n = int(n)

        print()

        menu[n-1][1](package_list)

        print()