from crud_business import valid_date
from package_reports_business import calculate_average, generate_period, calculate_destination


def calculate_destination_menu(package_list):
    """
    The semi-menu for the destination option
    :param package_list: PackageList
    :return: None
    """
    print("You selected to calculate the number of tour packages that have a specified destination")
    destination = input("Enter the desired destination: ")
    while destination == "":
        destination = input("Enter a valid destination: ")

    result = calculate_destination(package_list, destination.capitalize())

    print(f"The number of packages with the destination {destination.capitalize()} is {result}")


def generate_period_menu(package_list):
    """
    The semi-menu for the period option
    :param package_list: PackageList
    :return: None
    """
    print("You selected to generate a report with all the tour packages that are available in a specified period")
    start_date = input("Please enter the start date of the period: ")
    condition, feedback = valid_date(start_date)
    while not condition:
        start_date = input(f"The start date must {feedback}. Please enter again the start date(dd/mm/yyyy): ")
        condition, feedback = valid_date(start_date)

    finish_date = input("Please enter the finish date of the period: ")
    condition, feedback = valid_date(finish_date)
    while not condition:
        finish_date = input(f"The finish date must {feedback}. Please enter again the start date(dd/mm/yyyy): ")
        condition, feedback = valid_date(finish_date)

    report = generate_period(package_list, start_date, finish_date)

    if isinstance(report, str):
        print(report)
    else:
        print(f"Here is the report for the period {start_date} - {finish_date}:")
        for package in report:
            print(package)


def calculate_average_menu(package_list):
    """
    The semi-menu for the average option
    :param package_list: PackageList
    :return: None
    """
    print("You selected to calculate the average orice for a specific destination")
    destination = input("Enter the desired destination: ")
    while destination == "":
        destination = input("Enter a valid destination: ")

    average = calculate_average(package_list, destination.capitalize())
    print(f"The average price for the destination {destination} is {average}")

def generate_reports(package_list):
    """
    The main function that implements the functionality of the package reports feature
    :param package_list: PackageList
    :return: None

    """
    if not package_list:
        print("No tour packages available")
        return

    print("You selected option 5: getting reports")
    exit = input("If you want to go back to the main menu, press 5, else press Enter: ")
    if exit == "5":
        return
    print("You have 3 options: ")
    print("1. Calculating the number of tour packages that have a specified destination")
    print("2. Generating a report with all the tour packages that are available in a specified period")
    print("3. Calculating the average price for a specific destination")
    option = input("Please enter your option(must be an integer between 1 and 3): ")
    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 3)):
        option = input("Your option must be an integer between 1 and 3. Please enter again: ")

    if option == "1":
        calculate_destination_menu(package_list)
    elif option == "2":
        generate_period_menu(package_list)
    elif option == "3":
        calculate_average_menu(package_list)