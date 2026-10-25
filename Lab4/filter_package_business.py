def filter_destination_price(package_list, price, destination):
    """
    Returns the filtered array of packages that have the same destination as the destination parameter and have the
    price less than or equal to the price parameter
    :param package_list: List[Package]
    :param price: int
    :param destination: str
    :return: List[Package]
    """
    filtered_array = []
    for package in package_list.get_package_list():
        if package.price <= price or package.destination == destination:
            filtered_array.append(package)

    package_list.update_history()
    package_list.set_package_list(filtered_array)
    return filtered_array

def filter_month(package_list, month):
    """
    Returns an array with all the packages that don't have in their interval days in the same month as the month parameter
    :param package_list: List[Package]
    :param month: str
    :return: List[Package]
    """
    months_map = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8, "september": 9, "october": 10,
    "november": 11, "december": 12}
    filtered_array = []
    for package in package_list.get_package_list():
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

    package_list.update_history()
    package_list.set_package_list(filtered_array)
    return filtered_array
