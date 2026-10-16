from PackageClass import packages
from AddPackage import valid_date
from SearchPackages import contains

def calculate_destination(packages_list, destination):
    """
    Returns the packages that have the same destination as the destination paramater
    :param packages_list: List[Package]
    :param destination: str
    :return: int
    """
    counter = 0
    for package in packages:
        if package.destination == destination:
            counter += 1

    return counter

def calculate_destination_menu():
    """
    The semi-menu for the destination option
    :return: None
    """
    print("You selected to calculate the number of tour packages that have a specified destination")
    destination = input("Enter the desired destination: ")
    while destination == "":
        destination = input("Enter a valid destination: ")

    result = calculate_destination(packages, destination.capitalize())

    print(f"The number of packages with the destination {destination} is {result}")

def generate_period(packages_list, start_date, finish_date):
    """
    Returns a list containing all the packages that respect the period option
    :param packages_list: List[Package]
    :param start_date: str
    :param finish_date: str
    :return: List[Package] | str
    """
    report_list = []
    for package in packages:
        if contains(start_date, finish_date, package.start_date, package.end_date):
            report_list.append(package)

    return report_list if len(report_list) > 0 else "No packages found with the desired period"

def generate_period_menu():
    """
    The semi-menu for the period option
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

    report = generate_period(packages, start_date, finish_date)

    if isinstance(report, str):
        print(report)
    else:
        print(f"Here is the report for the period {start_date} - {finish_date}:")
        for package in report:
            print(package)

def calculate_average(packages_list, destination):
    """
    Calculates the average price for all the packages that have the destination parameter
    :param packages_list: List[Package]
    :param destination: str
    :return: float
    """
    average = 0
    counter = 0
    for package in packages_list:
        if package.destination == destination:
            average += package.price
            counter += 1

    return average / counter if counter > 0 else 0

def calculate_average_menu():
    """
    The semi-menu for the average option
    :return: None
    """
    print("You selected to calculate the average orice for a specific destination")
    destination = input("Enter the desired destination: ")
    while destination == "":
        destination = input("Enter a valid destination: ")

    average = calculate_average(packages, destination)
    print(f"The average price for the destination {destination} is {average}")

def generate_reports():
    """
    The main function that implements the functionality of the package reports feature
    :return: None

    """
    if not packages:
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
        calculate_destination_menu()
    elif option == "2":
        generate_period_menu()
    elif option == "3":
        calculate_average_menu()

