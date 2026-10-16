from Tests import test_valid_date, test_delete_destination
from AddPackage import add_package
from ModifyPackage import modify_package
from DeletePackages import delete_package
from SearchPackages import search_package
from PackageReports import generate_reports
from FilterPackage import filter_packages



def undo_operation():
    print("undo_operation")

def menu():
    """
    The implementation of the main menu
    :return: None
    """
    test_valid_date()
    test_delete_destination()

    print("Welcome to the travel agency app!")

    while True:
        print("Option 1: Add a tour package")
        print("Option 2: Modify a tour package")
        print("Option 3: Delete tour package")
        print("Option 4: Search for a tour package")
        print("Option 5: Get reports")
        print("Option 6: Filter packages")
        print("Option 7: Undo last operation")
        print("Option 8: Exit application")

        n = input("Enter the desired option: ")
        while not n.isdigit() or (n.isdigit() and (int(n) < 1 or int(n) > 8)):
            n = input("The option must be an integer between 1 and 8. Please enter again: ")
        n = int(n)

        print()

        if (n == 1):
            add_package()
        elif n == 2:
            modify_package()
        elif n == 3:
            delete_package()
        elif n == 4:
            search_package()
        elif n == 5:
            generate_reports()
        elif n == 6:
            filter_packages()
        elif n == 7:
            undo_operation()
        elif n == 8:
            print("App closed")
            exit()

        print()