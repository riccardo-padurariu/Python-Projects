from time import gmtime, strftime
import random

class Package():
    def __init__(self,start_date, finish_date, destination, price, id):
        self.start_date = start_date
        self.finish_date = finish_date
        self.destination = destination
        self.price = price
        self.id = id

    def __str__(self):
        return f"""
    Destination: {self.destination}
        From {self.start_date} to {self.finish_date}
        Price: {self.price}€
        Id: {self.id}"""

    def set_start_date(self,date):
        self.start_date = start_date

    def set_finish_date(self,date):
        self.finish_date = finish_date

    def set_destination(self, destination):
        self.destination = destination

    def set_price(self, price):
        self.price = price

packages = []

print("Welcome to the travel agency app!")

def valid_date(input_date, other_date = None):
    """
    Returns a tuple with a bool and a feedback, indicating the validness of the input_date
    :param input_date: str
    :param other_date: str | None
    :return: str
    """

    if not input_date or len(input_date.split("/")) != 3:
        return False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers"

    input_day, input_month, input_year = input_date.split("/")
    current_day, current_month, current_year = strftime("%d/%m/%Y", gmtime()).split("/")

    if not input_day.isdigit() or not input_month.isdigit() or not input_year.isdigit() or len(input_day) != 2 or len(input_month) != 2 or len(input_year) != 4:
        return False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers"


    input_day = int(input_day)
    input_month = int(input_month)
    input_year = int(input_year)

    current_day = int(current_day)
    current_month = int(current_month)
    current_year = int(current_year)

    if input_day > 31 or input_month > 13:
        return False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers"

    if current_year > input_year:
        return False, "be after the current date"
    elif current_year == input_year:
        if current_month > input_month:
            return False, "be after the current date"
        elif current_month == input_month:
            if current_day > input_day:
                return False, "be after the current date"

    if other_date:
        other_day, other_month, other_year = other_date.split("/")

        other_day = int(other_day)
        other_month = int(other_month)
        other_year = int(other_year)
        if other_year > input_year:
            return False, "be after the start date"
        elif other_year == input_year:
            if other_month > input_month:
                return False, "be after the start date"
            elif other_month == input_month:
                if other_day > input_day:
                    return False, "be after the start date"

    return True, ""



def get_date(status, other_date = None):
    """
    Returns a valid date from the user, using the other_date as a criteria when necessary
    :param status: str
    :param other_date: str
    :return: str
    """
    date = input(f"Enter the package {status} date(dd/mm/yyyy): ")
    condition, feedback = valid_date(date, other_date)
    while not condition:
        date = input(f"The {status} date must {feedback}. Please enter again the {status} date(dd/mm/yyyy): ")
        condition, feedback = valid_date(date, other_date)

    return date

def get_destination():
    destination = input("Enter the package destination: ")

    while destination == "":
        destination = input("Enter a valid destination: ")

    return destination.capitalize()

def get_price():
    price = input("Enter the package price: ")

    while not price.isdigit():
        price = input("The price must be an integer. Please enter again: ")

    return int(price)

def get_id():
    """
    Function that generates a random id for a new package
    :return: str
    """
    id = ""
    for i in range(10):
        id += str(random.randint(1,9))

    return id

def validate_input():
    """
    The function that validates the input for the add package feature
    :return: tuple(str, str, str, int, str)
    """
    start_date = get_date("start")
    finish_date = get_date("finish", start_date)
    destination = get_destination()
    price = get_price()
    id = get_id()

    return start_date, finish_date, destination, price, id


def add_package():
    """
    The main function that implements the functionality of the add package feature
    :return: None
    """
    print("You selected option 1: adding a tour package")
    exit = input("If you want to go back to the main menu, press 5, else press Enter: ")
    if exit == "5":
        return
    start_date, finish_date, destination, price, id = validate_input()
    package = Package(start_date, finish_date, destination, price, id)
    packages.append(package)

    print("The following package was added:")
    print(package)

def display_packages():
    for package in packages:
        print(package)

def exists(id):
    for index, package in enumerate(packages):
        if package.id == id:
            return True, index
    return False, -1

def get_selected_id(status):
    id = input(f"Please enter the id you want to {status}: ")
    condition, index = exists(id)
    while not condition:
        id = input(f"The id must exist. Please enter again the id of the package you want to {status}: ")
        condition, index = exists(id)

    return id, index


def choose_option():
    print("1. Start Date")
    print("2. Finish Date")
    print("3. Destination")
    print("4. Price")
    option = input("Choose the property you want to modify(from 1 to 4): ")

    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 4)):
        option = input("The option must be an integer between 1 and 4. Please enter again: ")

    return option

def set_new_date(index, id, status, other_date = None):
    print(f"You selected to modify the {status} date")
    date = (f"Please enter the new {status} date: ")
    condition, feedback = valid_date(date, other_date)
    while not condition:
        date = input(f"The {status} date must {feedback}. Please enter again the {status} date(dd/mm/yyyy): ")
        condition, feedback = valid_date(date, other_date)

    if status == "start":
        packages[index].set_start_date(date)
    elif status == "finish":
        packages[index].set_finish_date(date)
    print(f"Package {status} set to: {date}")

def set_destination(index, id):
    print("You selected to modify the destination property")
    destination = input("Please enter the new destination: ")
    while destination == "":
        destination = input("Enter a valid destination: ")

    packages[index].set_destination(destination.capitalize())
    print(f"Package destination set to: {destination}")

def set_price(index, id):
    print("You selected to modify the price property")
    price = input("Please enter the new price: ")
    while not price.isdigit() :
        price = input("The price must be a number. Please enter again: ")

    packages[index].set_price(price)
    print(f"Package price set to: {price}")

def modify_package():
    print("You selected option 2: modifying an existing tour package")
    exit = input("If you want to go back to the main menu, press 5, else press Enter: ")
    if exit == "5":
        return
    print("Those are the packages available:")
    display_packages()
    id, index = get_selected_id("modify")
    print(f"You selected the tour package with the Id {id}:")
    print(packages[index])

    option = choose_option()
    if option == "1":
        set_start_date(index, id)
    elif option == "2":
        set_finish_date(index, id, packages[index].start_date)
    elif option == "3":
        set_destination(index, id)
    elif option == "4":
        set_price(index, id)

    print("The package was modified successfully! Here is the updated version:")
    print(packages[index])


def delete_destination(package_list, destination):
    remaining_packages_id = []
    new_package_list = []
    for package in package_list:
        if package.destination != destination:
            remaining_packages_id.append(package.id)
            new_package_list.append(package)

    package_list = new_package_list
    return remaining_packages_id

def delete_destination_menu():
    print("You selected to delete all the packages that have a specified destination")
    destination = input("Please enter the name of the destination you want to delete: ").capitalize()
    if not exists_destination(destination):
        print(f"No destination with the name {destination}")
    delete_destination(packages, destination)

    print(f"Tour packages with the destination {destination} deleted successfully!")

def count_days(start, end):
    start_day, start_month, start_year = start.split("/")
    end_day, end_month, end_year = end.split("/")

    start_day, start_month, start_year = int(start_day), int(start_month), int(start_year)
    end_day, end_month, end_year = int(end_day), int(end_month), int(end_year)

    years = (end_year - start_year - 1)

    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    


def delete_days(packages_list, days):
    remaining_packages_id = []
    new_packages_list = []
    for package in packages_list:
        if count_days(package.start_date, package.finish_date) >= days:
            remaining_packages_id.append(package.id)
            new_packages_list.append(package)

    packages_list = new_packages_list
    return remaining_packages_id

def delete_days_menu():
    print("You selected to delete all the packages that last a shorter period than a specified number of days")
    days = input("Please enter the number of the days you want to use as threshold: ")
    while not days.isdigit():
        days = input("The number of days must be a positive integer. Please enter again: ")

    delete_days(packages, days)

    print(f"Tour packages with a shorter period than {days} deleted successfully!")


def delete_package():
    print("You selected option 3: deleting one or more existing tour packages")
    exit = input("If you want to go back to the main menu, press 5, else press Enter: ")
    if exit == "5":
        return
    print("You have 3 options: ")
    print("1. Deleting all the tour packages for a specified destination")
    print("2. Deleting all the tour packages that last a shorter period than a specified number of days")
    print("3. Deleting all the tour packages that have the price greater than a specified price")
    option = input("Please enter your option(must be an integer between 1 and 3): ")
    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 3)):
        option = input("Your option must be an integer between 1 and 3. Please enter again: ")

    if option == 1:
        delete_destination_menu()
    elif option == 2:
        delete_period()
    elif option == 3:
        delete_price()

    print("Package/packages deleted successfully!")

def search_package():
    print("search_package")

def generate_reports():
    print("generate_reports")

def filter_packages():
    print("filter_packages")

def undo_operation():
    print("undo_operation")

# Tests for the testable functions

def test_delete_destination():
    assert delete_destination([
    Package("12/12/2026", "15/12/2026", "Paris", "3000", "12355261"),
    Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
    Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
    Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
    Package("12/04/2027", "18/04/2027", "Ibiza", "5200", "38163496")],
    "Paris") == ["41235113", "23959873", "38163496"]
    assert delete_destination([
    Package("15/12/2026", "19/12/2026", "Canada", "3050", "72252463"),
    Package("11/11/2026", "18/11/2026", "Zimbawe", "2800", "13463571"),
    Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
    Package("20/01/2027", "28/01/2027", "Canada", "4500", "13743521"),
    Package("14/02/2027", "24/02/2027", "Rio de Janeiro", "5200", "16346134")],
    "Canada") == ["13463571", "12455242", "16346134"]
    assert delete_destination([
    Package("23/10/2026", "31/10/2026", "Oslo", "3000", "12492353"),
    Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
    Package("07/06/2027", "14/07/2027", "Paris", "3500", "12423461"),
    Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
    Package("12/04/2027", "18/04/2027", "Oslo", "5200", "38163496")],
    "Oslo") == ["41235113", "12423461", "23959873"]
    assert delete_destination([
    Package("12/12/2026", "15/12/2026", "Tenerife", "3000", "12355261"),
    Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
    Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
    Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
    Package("12/04/2027", "18/04/2027", "Tenerife", "5200", "38163496")],
    "Tenerife") == ["41235113", "12455242"]

def test_valid_date():
    assert valid_date("12/04/12e1") == (False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers")
    assert valid_date("17/07/2026") == (False, "be after the current date")
    assert valid_date("15/10/2026", "20/10/2026") == (False, "be after the start date")
    assert valid_date("31/10/2026") == (True, "")
    assert valid_date("12/21/2026") == (False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers")
    assert valid_date("12/12/202") == (False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers")
    assert valid_date("/04/2002","12/01/2027") == (False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers")
    assert valid_date("25/12/2026") == (True, "")
    assert valid_date("") == (False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers")

def menu():

    test_valid_date()
    test_delete_destination()

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



menu()