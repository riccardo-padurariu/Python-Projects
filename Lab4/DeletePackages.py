from PackageClass import Package, packages

def delete_destination(package_list, destination):
    """
    Pops out of the package_list all the tour packages in which the destination is the same as the destination parameter.
    Returns a list of the id's that remained in the list
    :param package_list: List[Package]
    :param destination:str
    :return: List[str]
    """
    remaining_packages_id = []
    new_package_list = []
    for package in package_list:
        if package.destination != destination:
            remaining_packages_id.append(package.id)
            new_package_list.append(package)

    package_list[:] = new_package_list
    return remaining_packages_id

def exists_destination(packages_list, destination):
    """
    Return a boolean semnificating the existence of a destination in the packages_list
    :param packages_list: List[Package]
    :param destination: str
    :return: boolean
    """
    for package in packages_list:
        if package.destination == destination:
            return True

    return False

def delete_destination_menu():
    """
    The sub-menu for the delete destination option
    :return: None
    """
    print("You selected to delete all the packages that have a specified destination")
    destination = input("Please enter the name of the destination you want to delete: ").capitalize()
    if not exists_destination(packages, destination):
        print(f"No destination with the name {destination}")
        return
    delete_destination(packages, destination)

    print(f"Tour packages with the destination {destination} deleted successfully!")


def count_days(start, end):
    """
    Returns the distance in days between the start and end dates
    :param start: str
    :param end: str
    :return: int
    """
    start_day, start_month, start_year = start.split("/")
    end_day, end_month, end_year = end.split("/")

    start_day, start_month, start_year = int(start_day), int(start_month), int(start_year)
    end_day, end_month, end_year = int(end_day), int(end_month), int(end_year)

    days = 0
    if start_year == end_year:

        days = 365 * (end_year - start_year - 1)

        months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        for month in range(start_month+1, 13):
            days += months[month]

        days += months[start_month] - start_day + 1

        for month in range(1,end_month):
            days += months[month]

        days += end_day
    else:
        days = 0
        for month in range(start_month+1, end_month):
            days += months[month]

        if start_month != end_month:
            days += month[start_month] - start_day + 1
            days += end_day
        else:
            days += end_day - start_day + 1

    return days

def delete_days(packages_list, days):
    """
    Pops out of the packages_list all the packages in which the distance in days is less than the days parameter.
    Returns the array formed by the remaining id's
    :param packages_list: List[Package]
    :param days: int
    :return: List[str]
    """
    remaining_packages_id = []
    new_packages_list = []
    for package in packages_list:
        if count_days(package.start_date, package.finish_date) >= days:
            remaining_packages_id.append(package.id)
            new_packages_list.append(package)

    packages[:] = new_packages_list
    return remaining_packages_id


def delete_days_menu():
    """
    The sub-menu for the delete days option
    :return: None
    """
    print("You selected to delete all the packages that last a shorter period than a specified number of days")
    days = input("Please enter the number of the days you want to use as a threshold: ")
    while not days.isdigit():
        days = input("The number of days must be a positive integer. Please enter again: ")

    delete_days(packages, int(days))

    print(f"Tour packages with a shorter period than {days} deleted successfully!")

def delete_price(packages_list, price):
    """
    Pops out of the packages_list the packages which have the price greater than the price parameter.
    Returns an array with the remaining packages id's
    :param packages_list: List[Package]
    :param price: int
    :return: List[str]
    """
    new_packages_list = []
    remaining_packages_id = []
    for package in packages_list:
        if package.price <= price:
            remaining_packages_id.append(package.id)
            new_packages_list.append(package)

    packages[:] = new_packages_list
    return remaining_packages_id


def delete_price_menu():
    """
    The sub-menu for the delete price option
    :return: None
    """
    print("You selected to delete all the packages that have the price greater than a specified price")
    price = input("Please enter the price that you want to use as a threshold: ")
    while not price.isdigit():
        price = input("The price must be a positive integer. Please try again: ")

    delete_price(packages, int(price))

    print(f"Tour packages with a greater price than {price} deleted successfully!")

def delete_package():
    """
    The main function that implements the functionality of the delete package feature
    :return: None
    """
    if not packages:
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

    condition = False
    if option == "1":
        delete_destination_menu()
    elif option == "2":
        delete_days_menu()
    elif option == "3":
        delete_price_menu()
