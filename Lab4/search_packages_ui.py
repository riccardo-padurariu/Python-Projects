from crud_business import valid_date
from search_packages_business import search_interval, search_destination_price, search_finish_date


def search_interval_menu(package_list):
    """
    The semi-menu for the search interval option
    :param package_list: List[Package]
    :return: None
    """
    print("You selected to search all the tour packages that are taking place in a specific interval of time")
    start_date = input("Enter the start date for the interval(dd/mm/yyyy): ")
    condition, feedback = valid_date(start_date)
    while not condition:
        start_date = input(f"The start date must {feedback}. Please enter again the start date(dd/mm/yyyy): ")
        condition, feedback = valid_date(start_date)

    finish_date = input("Enter the finish date for the interval(dd/mm/yyyy): ")
    condition, feedback = valid_date(finish_date, start_date)
    while not condition:
        finish_date = input(f"The finish date must {feedback}. Please enter again the finish date(dd/mm/yyyy): ")
        condition, feedback = valid_date(finish_date, start_date)

    search_result = search_interval(package_list.get_package_list(), start_date, finish_date)
    if isinstance(search_result, str):
        print(search_result)
    else:
        print("Here are the results of your search: ")
        for package in search_result:
            print(package)

def search_destination_price_menu(package_list):
    """
    The semi-menu for the search destination and price option
    :param package_list: List[Package]
    :return: None
    """
    print("You selected to search all the tour packages with a specific destination and a price within a selected price")
    destination = input("Enter the desired destination to search: ")
    while destination == "":
        destination = input("Enter a valid destination: ")

    destination = destination.capitalize()

    price = input("Enter the price: ")
    while not price.isdigit():
        price = input("The price must be a positive integer. Please enter again: ")
    price = int(price)

    search_result = search_destination_price(package_list.get_package_list(), destination, price)
    if isinstance(search_result, str):
        print(search_result)
    else:
        print("Here are the results of your search: ")
        for package in search_result:
            print(package)

def search_finish_date_menu(package_list):
    """
    The semi-menu for the search finish date option
    :param package_list: List[Package]
    :return: None
    """
    print("You selected to search all the tour packages that have a specified finish date")
    finish_date = input("Enter the desired finish date for the search: ")
    condition, feedback = valid_date(finish_date)
    while not condition:
        finish_date = input(f"The finish date must {feedback}. Please enter again the finish date(dd/mm/yyyy): ")
        condition, feedback = valid_date(finish_date)

    search_result = search_finish_date(package_list.get_package_list(), finish_date)

    if isinstance(search_result, str):
        print(search_result)
    else:
        print("Here are the results of your search: ")
        for package in search_result:
            print(package)

def search_package(package_list):
    """
    The main function that implements the functionality of the search package feature
    :param package_list: PackageList
    :return: None
    """
    if not package_list.get_package_list():
        print("No tour packages available")
        return

    print("You selected option 4: searching one or more existing tour packages")
    exit = input("If you want to go back to the main menu, press 5, else press Enter: ")
    if exit == "5":
        return
    print("You have 3 options: ")
    print("1. Searching all the tour packages that are taking place in a specific interval of time")
    print("2. Searching all the tour packages with a specific destination and a price within a selected price")
    print("3. Searching all the tour packages that have a specified finish date")
    option = input("Please enter your option(must be an integer between 1 and 3): ")
    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 3)):
        option = input("Your option must be an integer between 1 and 3. Please enter again: ")

    condition = False
    if option == "1":
        search_interval_menu(package_list)
    elif option == "2":
        search_destination_price_menu(package_list)
    elif option == "3":
        search_finish_date_menu(package_list)