from PackageClass import Package, packages
from time import gmtime, strftime
import random

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
    """
    Returns a valid destination for the new tour package
    :return: str
    """
    destination = input("Enter the package destination: ")

    while destination == "":
        destination = input("Enter a valid destination: ")

    return destination.capitalize()

def get_price():
    """
    Returns a valid price for the new tour package
    :return: int
    """
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
