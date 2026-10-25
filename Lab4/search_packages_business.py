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

def search_interval(package_list, start_date, finish_date):
    """
    Returns an array that contains all the packages in which the interval (package.start_date, package.finish_date)
    is included in the interval (start_date, finish_date), a string if the search array is empty
    :param package_list: List[Package]
    :param start_date: str
    :param finish_date: str
    :return: List[Package] | str
    """
    search_list = []
    for package in package_list:
        if contains(start_date, finish_date, package.start_date, package.finish_date):
            search_list.append(package)

    return search_list if len(search_list) > 0 else "No packages matched the search filters"

def search_destination_price(package_list, destination, price):
    """
    Returns an array that contains all the packages in which the destination is equal to the destination parameter
    and the price is less than or equal to the price, a string if the search array is empty
    :param package_list: List[Package]
    :param destination: str
    :param price: int
    :return: List[Package] | str
    """
    search_result = []
    for package in package_list:
        if package.destination == destination and package.price <= price:
            search_result.append(package)

    return search_result if len(search_result) > 0 else "No packages matched the search filters"

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

