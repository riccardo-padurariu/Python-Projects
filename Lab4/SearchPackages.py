from AddPackage import valid_date
from PackageClass import packages

def contains(lower_bound, upper_bound, start_date, finish_date):
    """
    Returns a boolean indicating if the interval formed by the dates (start_date, finish_date) is included in the
    interval formed by the dates (lower_bound, upper_bound)
    :param lower_bound: str
    :param upper_bound: str
    :param start_date: str
    :param finish_date: str
    :return: boolean
    """
    lower_bound = lower_bound.split("/")
    lower_bound = {
        "day": int(lower_bound[0]),
        "month": int(lower_bound[1]),
        "year": int(lower_bound[2])
    }

    upper_bound = upper_bound.split("/")
    upper_bound = {
        "day": int(upper_bound[0]),
        "month": int(upper_bound[1]),
        "year": int(upper_bound[2])
    }

    start_date = start_date.split("/")
    start_date = {
        "day": int(start_date[0]),
        "month": int(start_date[1]),
        "year": int(start_date[2])
    }

    finish_date = finish_date.split("/")
    finish_date = {
        "day": int(finish_date[0]),
        "month": int(finish_date[1]),
        "year": int(finish_date[2])
    }

    if lower_bound["year"] > start_date["year"]:
        return False
    elif lower_bound["year"] == start_date["year"]:
        if lower_bound["month"] > start_date["month"]:
            return False
        elif lower_bound["month"] == start_date["month"]:
            if lower_bound["day"] > start_date["day"]:
                return False

    if finish_date["year"] > upper_bound["year"]:
        return False
    elif finish_date["year"] == upper_bound["year"]:
        if finish_date["month"] > upper_bound["month"]:
            return False
        elif finish_date["month"] == upper_bound["month"]:
            if finish_date["day"] > upper_bound["day"]:
                return False

    return True

def search_interval(start_date, finish_date):
    """
    Returns an array that contains all the packages in which the interval (package.start_date, package.finish_date)
    is included in the interval (start_date, finish_date), a string if the search array is empty
    :param start_date: str
    :param finish_date: str
    :return: List[Package] | str
    """
    search_list = []
    for package in packages:
        if contains(start_date, finish_date, package.start_date, package.finish_date):
            search_list.append(package)

    return search_list if len(search_list) > 0 else "No packages matched the search filters"

def search_interval_menu():
    """
    The semi-menu for the search interval option
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

    search_result = search_interval(start_date, finish_date)
    if isinstance(search_result, str):
        print(search_result)
    else:
        print("Here are the results of your search: ")
        for package in search_result:
            print(package)

def search_destination_price(packages_list, destination, price):
    """
    Returns an array that contains all the packages in which the destination is equal to the destination parameter
    and the price is less than or equal to the price, a string if the search array is empty
    :param packages_list: List[Package]
    :param destination: str
    :param price: int
    :return: List[Package] | str
    """
    search_result = []
    for package in packages_list:
        if package.destination == destination and package.price <= price:
            search_result.append(package)

    return search_result if len(search_result) > 0 else "No packages matched the search filters"

def search_destination_price_menu():
    """
    The semi-menu for the search destination and price option
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

    search_result = search_destination_price(packages, destination, price)
    if isinstance(search_result, str):
        print(search_result)
    else:
        print("Here are the results of your search: ")
        for package in search_result:
            print(package)

def search_finish_date(packages_list, finish_date):
    """
    Returns an array in which each package have the same finish_date as the finish_date parameter.
    Returns a string if the searched array is empty
    :param packages_list: List[Package]
    :param finish_date: str
    :return: List[Package] | str
    """
    search_result = []
    for package in packages_list:
        if package.finish_date == finish_date:
            search_result.append(package)

    return search_result if len(search_result) > 0 else "No packages matched the search filters"

def search_finish_date_menu():
    """
    The semi-menu for the search finish date option
    :return: None
    """
    print("You selected to search all the tour packages that have a specified finish date")
    finish_date = input("Enter the desired finish date for the search: ")
    condition, feedback = valid_date(finish_date)
    while not condition:
        finish_date = input(f"The finish date must {feedback}. Please enter again the finish date(dd/mm/yyyy): ")
        condition, feedback = valid_date(finish_date)

    search_result = search_finish_date(packages, finish_date)

    if isinstance(search_result, str):
        print(search_result)
    else:
        print("Here are the results of your search: ")
        for package in search_result:
            print(package)


def search_package():
    """
    The main function that implements the functionality of the search package feature
    :return: None
    """
    if not packages:
        print("No tour packages available")
        return

    print("You selected option 3: searching one or more existing tour packages")
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
        search_interval_menu()
    elif option == "2":
        search_destination_price_menu()
    elif option == "3":
        search_finish_date_menu()
