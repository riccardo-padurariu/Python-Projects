from crud_business import valid_date
from search_packages_business import contains

def calculate_destination(package_list, destination):
    """
    Returns the packages that have the same destination as the destination paramater
    :param package_list: PackageList
    :param destination: str
    :return: int
    """
    counter = 0
    for package in package_list.get_package_list():
        if package.destination == destination:
            counter += 1

    return counter

def generate_period(package_list, start_date, finish_date):
    """
    Returns a list containing all the packages that respect the period option
    :param package_list: PackageList
    :param start_date: str
    :param finish_date: str
    :return: List[Package] | str
    """
    report_list = []
    for package in package_list.get_package_list():
        if contains(start_date, finish_date, package.start_date, package.finish_date):
            report_list.append(package)

    return report_list if len(report_list) > 0 else "No packages found with the desired period"

def calculate_average(packages_list, destination):
    """
    Calculates the average price for all the packages that have the destination parameter
    :param packages_list: PackageList
    :param destination: str
    :return: float
    """
    average = 0
    counter = 0
    for package in packages_list.get_package_list():
        if package.destination == destination:
            average += package.price
            counter += 1

    return average / counter if counter > 0 else 0

