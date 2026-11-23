from domain import PackageList, Package
from package_reports_business import calculate_destination, generate_period, calculate_average


def test_calculate_destination():
    """
    Testing the calculate_destination() function
    :return: None
    """
    package_list = PackageList()
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package2 = Package("11/11/2026", "18/11/2026", "London", 3000, "13542414")
    package3 = Package("04/03/2027", "12/03/2027", "Roma", 4500, "18423252")
    package_list.set_package_list([package, package2, package3])
    assert calculate_destination(package_list, "Paris") == 1
    package4 = Package("01/07/2027", "10/07/2027", "Roma", 4500, "19423652")
    package_list.add_package(package4)
    assert calculate_destination(package_list,"Roma") == 2
    assert calculate_destination(package_list,"Sicilia") == 0

def test_generate_period():
    """
    Testing the generate_period() function
    :return: None
    """
    package_list = PackageList()
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package2 = Package("11/11/2026", "18/11/2026", "London", 3000, "13542414")
    package3 = Package("04/03/2027", "12/03/2027", "Roma", 4500, "18423252")
    package_list.set_package_list([package, package2, package3])
    assert generate_period(package_list,"01/01/2027","12/01/2027") == "No packages found with the desired period"
    assert generate_period(package_list,"03/03/2027","15/03/2027") == [package3]
    package4 = Package("01/12/2026", "10/12/2026", "Roma", 4500, "19423652")
    package_list.add_package(package4)
    assert generate_period(package_list,"01/12/2026","01/01/2027") == [package, package4]
    assert generate_period(package_list,"02/11/2026","15/03/2027") == [package, package2, package3, package4]

def test_calculate_average():
    """
    Testing the calculate_average() function
    :return: None
    """
    package_list = PackageList()
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package2 = Package("11/11/2026", "18/11/2026", "Paris", 3000, "13542414")
    package3 = Package("04/03/2027", "12/03/2027", "Roma", 4500, "18423252")
    package_list.set_package_list([package, package2, package3])
    assert calculate_average(package_list, "Paris") == 2750
    assert calculate_average(package_list, "Roma") == 4500
    assert calculate_average(package_list, "London") == 0
    package4 = Package("01/12/2026", "10/12/2026", "Roma", 4500, "19423652")
    package_list.add_package(package4)
    assert calculate_average(package_list, "Roma") == 4500
    assert calculate_average(package_list, "Sicilia") == 0


def test_reports():
    """
    This function tests the entire package reports functionality
    :return: None
    """
    test_calculate_destination()
    test_generate_period()
    test_calculate_average()