from PackageClass import packages

def filter_destination_price(packages_list, price, destination):
    """
    Returns the filtered array of packages that have the same destination as the destination parameter and have the
    price less than or equal to the price parameter
    :param packages_list: List[Package]
    :param price: int
    :param destination: str
    :return: List[Package]
    """
    filtered_array = []
    for package in packages_list:
        if package.price <= price or package.destination == destination:
            filtered_array.append(package)

    packages_list[:] = filtered_array
    return filtered_array

def filter_destination_price_menu():
    """
    The semi-menu for the destination and price option
    :return: None
    """
    print("You selected to filter out the packages that have a price greater than a specified one and a destination different than the one read as input")
    price = input("Enter the price that it will be used as threshold: ")
    while not price.isdigit():
        price = input("The price must be a positive integer. Please enter again: ")

    destination = input("Enter the destination: ")
    while destination == "":
        destination = input("Enter a valid destination: ")

    filtered_array = filter_destination_price(packages, int(price), destination.capitalize())
    print("Packages filtered successfully!")

def filter_month(packages_list, month):
    """
    Returns an array with all the packages that don't have in their interval days in the same month as the month parameter
    :param packages_list: List[Package]
    :param month: str
    :return: List[Package]
    """
    months_map = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8, "september": 9, "october": 10,
    "november": 11, "december": 12}
    filtered_array = []
    for package in packages_list:
        start_month = int(package.start_date.split("/")[1])
        finish_month = int(package.finish_date.split("/")[1])
        start_year = int(package.start_date.split("/")[1])
        finish_year = int(package.finish_date.split("/")[1])
        if start_year == finish_year:
            if start_month > finish_month:
                start_month, finish_month = finish_month, start_month
            if not (start_month <= months_map[month] and months_map[month] <= finish_month):
                filtered_array.append(package)
        elif finish_year - start_year == 1:
            if not (start_month <= months_map[month] and months_map[month] <= finish_month):
                filtered_array.append(package)

    packages_list[:] = filtered_array
    return filtered_array



def filter_month_menu():
    """
    The semi-menu for the month option
    :return: None
    """
    print("You selected to filter out the packages that have in their interval days from a specific month")
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    month = input("Enter the month: ")
    while month.lower() not in months:
        month = input("Enter a valid month: ")

    filtered_array = filter_month(packages, month)

def filter_packages():
    """
    The main function that implements the functionality of the filter packages feature
    :return: None
    """
    if not packages:
        print("No tour packages available")
        return

    print("You selected option 6: filtering packages")
    exit = input("If you want to go back to the main menu, press 5, else press Enter: ")
    if exit == "5":
        return
    print("You have 2 options: ")
    print("1. Filtering out the packages that have a price greater than a specified one and a destination different than the one read as input")
    print("2. Filtering out the packages that have in their period days from a specific month")
    option = input("Please enter your option(must be an integer between 1 and 2): ")
    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 2)):
        option = input("Your option must be an integer between 1 and 2. Please enter again: ")

    if option == "1":
        filter_destination_price_menu()
    elif option == "2":
        filter_month_menu()