from domain import Package
from crud_business import get_id, valid_date, exists_destination, delete_destination, delete_days, delete_price


def add_package(package_list):
    """
    The main function that implements the functionality of the add package feature
    :param package_list: PackageList
    :return: None
    """
    print("You selected option 1: adding a tour package")
    exit = input("If you want to go back to the main menu, press 5, else press Enter: ")
    if exit == "5":
        return
    start_date, finish_date, destination, price, id = validate_input()
    package = Package(start_date, finish_date, destination, price, id)
    package_list.add_package(package)

    print("The following package was added:")
    print(package)
    print("-------------------------------------------")
    print("The current packages are: ")
    display_packages(package_list)
    print("-------------------------------------------")

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

def get_price():
    """
    Returns a valid price for the new tour package
    :return: int
    """
    price = input("Enter the package price: ")

    while not price.isdigit():
        price = input("The price must be an integer. Please enter again: ")

    return int(price)

def get_destination():
    """
    Returns a valid destination for the new tour package
    :return: str
    """
    destination = input("Enter the package destination: ")

    while destination == "":
        destination = input("Enter a valid destination: ")

    return destination.capitalize()

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



def display_packages(package_list):
    """
    Displays the packages
    :param package_list: PackageList
    :return: None
    """
    for package in package_list.get_package_list():
        print(package)

def get_selected_id(package_list, status):
    """
    Returns a tuple containing an existing id from the user and it's position in the packages list
    :param package_list: PackageList
    :param status: str
    :return: str
    """
    id = input(f"Please enter the id you want to {status}: ")
    condition = package_list.exists_id(id)[0]
    while not condition:
        id = input(f"The id must exist. Please enter again the id of the package you want to {status}: ")
        condition = package_list.exists_id(id)[0]

    return id

def choose_option():
    """
    Gets a valid option for the user to modify the corresponding package
    :return: str
    """
    print("1. Start Date")
    print("2. Finish Date")
    print("3. Destination")
    print("4. Price")
    option = input("Choose the property you want to modify(from 1 to 4): ")

    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 4)):
        option = input("The option must be an integer between 1 and 4. Please enter again: ")

    return option

def set_new_date(package_list, id, status, other_date = None, finish_date = None):
    """
    Sets the start_date or finish_date(depends on the status) of the package corresponding
    to the id to a valid date got as input from the user. It uses the other_date if it's
    setting the finish_date, the other_date being the current start_date
    :param package_list: PackageList
    :param id: str
    :param status: str
    :param other_date: str | None
    :param finish_date: str | None
    :return: None
    """
    print(f"You selected to modify the {status} date")
    date = input(f"Please enter the new {status} date: ")
    condition, feedback = valid_date(date, other_date, finish_date)
    while not condition:
        date = input(f"The {status} date must {feedback}. Please enter again the {status} date(dd/mm/yyyy): ")
        condition, feedback = valid_date(date, other_date, finish_date)

    if status == "start":
        package_list.set_package_attribute(id, "start_date", date)
        #package_list.get_package(id).set_start_date(date)
    elif status == "finish":
        package_list.set_package_attribute(id, "finish_date", date)
        #package_list.get_package(id).set_finish_date(date)
    print(f"Package {status} set to: {date}")

def set_destination(package_list, id):
    """
    Sets the destination of the package corresponding to the id parameter, destination got as input from the user
    :param package_list: PackageList
    :param id: str
    :return: None
    """
    print("You selected to modify the destination property")
    destination = input("Please enter the new destination: ")
    while destination == "":
        destination = input("Enter a valid destination: ")

    package_list.set_package_attribute(id, "destination", destination.capitalize())
    print(f"Package destination set to: {destination}")

def set_price(package_list, id):
    """
    Sets the price of the package corresponding to the id parameter, price got as input from the user
    :param package_list: PackageList
    :param id: str
    :return: None
    """
    print("You selected to modify the price property")
    price = input("Please enter the new price: ")
    while not price.isdigit() :
        price = input("The price must be a number. Please enter again: ")

    package_list.set_package_attribute(id, "price", price)
    print(f"Package price set to: {price}")

def modify_package(package_list):
    """
    The main function that implements the functionality of the modify package feature
    :param package_list: PackageList
    :return: None
    """
    if not package_list.get_package_list():
        print("No tour packages available")
        return

    print("You selected option 2: modifying an existing tour package")
    exit = input("If you want to go back to the main menu, press 5, else press Enter: ")
    if exit == "5":
        return
    print("Those are the packages available:")
    display_packages(package_list)
    id = get_selected_id(package_list,"modify")
    print(f"You selected the tour package with the Id {id}:")
    print(package_list.get_package(id))

    package_list.update_history()

    option = choose_option()
    match option:
        case "1":
            set_new_date(package_list, id, "start", None, package_list.get_package(id).get_finish_date())
        case "2":
            set_new_date(package_list, id, "finish", package_list.get_package(id).get_start_date())
        case "3":
            set_destination(package_list, id)
        case "4":
            set_price(package_list, id)

    print("-------------------------------------------------------------------")
    print("The package was modified successfully! Here is the updated version:")
    print(package_list.get_package(id))
    print("-------------------------------------------------------------------")



def delete_destination_menu(package_list):
    """
    The sub-menu for the delete destination option
    :param package_list: PackageList
    :return: None
    """
    print("You selected to delete all the packages that have a specified destination")
    destination = input("Please enter the name of the destination you want to delete: ").capitalize()
    while destination == "":
        destination = input("Enter a valid destination: ")

    if not exists_destination(package_list, destination):
        print(f"No destination with the name {destination}")
        return
    delete_destination(package_list, destination)

    print(f"Tour packages with the destination {destination} deleted successfully!")


def delete_days_menu(package_list):
    """
    The sub-menu for the delete days option
    :param package_list: PackageList
    :return: None
    """
    print("You selected to delete all the packages that last a shorter period than a specified number of days")
    days = input("Please enter the number of the days you want to use as a threshold: ")
    while not days.isdigit():
        days = input("The number of days must be a positive integer. Please enter again: ")

    delete_days(package_list, int(days))

    print(f"Tour packages with a shorter period than {days} deleted successfully!")



def delete_price_menu(package_list):
    """
    The sub-menu for the delete price option
    :param package_list: PackageList
    :return: None
    """
    print("You selected to delete all the packages that have the price greater than a specified price")
    price = input("Please enter the price that you want to use as a threshold: ")
    while not price.isdigit():
        price = input("The price must be a positive integer. Please try again: ")

    delete_price(package_list, int(price))

    print(f"Tour packages with a greater price than {price} deleted successfully!")


def delete_package(package_list):
    """
    The main function that implements the functionality of the delete package feature
    :param package_list: PackageList
    :return: None
    """
    if not package_list.get_package_list():
        print("No tour packages available")
        return

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

    if option == "1":
        delete_destination_menu(package_list)
    elif option == "2":
        delete_days_menu(package_list)
    elif option == "3":
        delete_price_menu(package_list)