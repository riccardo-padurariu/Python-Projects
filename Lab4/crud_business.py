from time import gmtime, strftime
import random

# The add package section

def valid_date(input_date, other_date = None, finish_date = None):
    """
    Returns a tuple with a bool and a feedback, indicating the validness of the input_date
    :param input_date: str
    :param other_date: str | None
    :param finish_date: str | None
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

    if finish_date:
        finish_day, finish_month, finish_year = finish_date.split("/")

        finish_day = int(finish_day)
        finish_month = int(finish_month)
        finish_year = int(finish_year)
        if input_year > finish_year:
            return False, "be before the finish date"
        elif input_year == finish_year:
            if input_month > finish_month:
                return False, "be before the finish date"
            elif input_month == finish_month:
                if input_day > finish_day:
                    return False, "be before the finish date"


    return True, ""

def get_id():
    """
    Function that generates a random id for a new package
    :return: str
    """
    id = ""
    for i in range(10):
        id += str(random.randint(1,9))

    return id


# The delete package section

def delete_destination(package_list, destination):
    """
    Pops out of the package_list all the tour packages in which the destination is the same as the destination parameter.
    Returns a list of the id's that remained in the list
    :param package_list: PackageList
    :param destination: str
    :return: List[str]
    """
    remaining_packages_id = []
    new_package_list = []
    for package in package_list.get_package_list():
        if package.destination != destination:
            remaining_packages_id.append(package.id)
            new_package_list.append(package)

    package_list.set_package_list(new_package_list)
    return remaining_packages_id

def exists_destination(package_list, destination):
    """
    Return a boolean semnificating the existence of a destination in the packages_list
    :param package_list: PackageList
    :param destination: str
    :return: boolean
    """
    for package in package_list.get_package_list():
        if package.destination == destination:
            return True

    return False

def is_bisect(year):
    return year % 4 == 0 and (year % 100 == 0 and year % 400 == 0)

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
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if start_year == end_year:

        days = 365 * (end_year - start_year - 1)


        for month in range(start_month+1, 13):
            days += months[month]

        days += months[start_month] - start_day + 1

        for month in range(1,end_month):
            days += months[month]

        days += end_day
    else:
        if start_month != end_month:
            days += months[start_month] - start_day + 1
            days += end_day
        else:
            days += end_day - start_day + 1

        for month in range(start_month+1, end_month):
            days += months[month]

    for year in range(start_year,end_year):
        if is_bisect(year):
            days += 1

    return days

def delete_days(package_list, days):
    """
    Pops out of the packages_list all the packages in which the distance in days is less than the days parameter.
    Returns the array formed by the remaining id's
    :param package_list: PackageList
    :param days: int
    :return: List[str]
    """
    remaining_packages_id = []
    new_packages_list = []
    for package in package_list.get_package_list():
        if count_days(package.start_date, package.finish_date) >= days:
            remaining_packages_id.append(package.id)
            new_packages_list.append(package)

    package_list.set_package_list(new_packages_list)
    return remaining_packages_id


def delete_price(package_list, price):
    """
    Pops out of the packages_list the packages which have the price greater than the price parameter.
    Returns an array with the remaining packages id's
    :param package_list: List[Package]
    :param price: int
    :return: List[str]
    """
    new_packages_list = []
    remaining_packages_id = []
    for package in package_list.get_package_list():
        if package.price <= price:
            remaining_packages_id.append(package.id)
            new_packages_list.append(package)

    package_list.set_package_list(new_packages_list)
    return remaining_packages_id
