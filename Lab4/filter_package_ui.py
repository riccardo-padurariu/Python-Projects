from filter_package_business import filter_destination_price, filter_month

def filter_destination_price_menu(package_list):
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

    filtered_array = filter_destination_price(package_list, int(price), destination.capitalize())
    print("Packages filtered successfully!")

def filter_month_menu(package_list):
    """
    The semi-menu for the month option
    :return: None
    """
    print("You selected to filter out the packages that have in their interval days from a specific month")
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    month = input("Enter the month: ")
    while month.lower() not in months:
        month = input("Enter a valid month: ")

    filtered_array = filter_month(package_list, month)
    print("Packages filtered successfully!")

def filter_packages(package_list):
    """
    The main function that implements the functionality of the filter packages feature
    :return: None
    """
    if not package_list.get_package_list():
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
        filter_destination_price_menu(package_list)
    elif option == "2":
        filter_month_menu(package_list)