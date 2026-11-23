from domain import PackageList, Package
from search_packages_business import contains, search_interval, search_destination_price, search_finish_date


def test_contains():
    """
    Testing the contains() function
    :return: None
    """
    assert contains("12/12/2026","31/12/2026","15/12/2026","20/12/2026") == True
    assert contains("03/04/2027","12/04/2027","04/04/2027","10/04/2027") == True
    assert contains("01/02/2027","12/02/2027","10/02/2027","20/02/2027") == False
    assert contains("03/10/2027","20/10/2027","18/10/2027","25/10/2027") == False
    assert contains("12/04/2027","18/04/2027","15/04/2027","18/04/2027") == True

def test_search_interval():
    """
    Testing the search_interval() function
    :return: None
    """
    package_list = PackageList()
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package2 = Package("11/11/2026", "18/11/2026", "London", 3000, "13542414")
    package3 = Package("04/03/2027", "12/03/2027", "Roma", 4500, "18423252")
    package_list.set_package_list([package, package2, package3])
    assert search_interval(package_list, "01/11/2026","01/01/2027") == [package, package2]
    assert search_interval(package_list, "01/01/2027","15/03/2027") == [package3]
    package4 = Package("11/08/2027","18/08/2027","Sicilia",3500,"12435125")
    package_list.add_package(package4)
    assert search_interval(package_list,"01/03/2027","31/08/2027") == [package3, package4]
    assert search_interval(package_list,"01/01/2027","15/01/2027") == "No packages matched the search filters"

def test_search_destination_price():
    """
    Testing the search_destination_price() function
    :return: None
    """
    package_list = PackageList()
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package2 = Package("11/11/2026", "18/11/2026", "Paris", 3000, "13542414")
    package3 = Package("04/03/2027", "12/03/2027", "Roma", 4500, "18423252")
    package_list.set_package_list([package, package2, package3])
    assert search_destination_price(package_list,"Paris",2700) == [package]
    assert search_destination_price(package_list,"Paris",3100) == [package, package2]
    assert search_destination_price(package_list,"Roma", 4000) == "No packages matched the search filters"
    package4 = Package("11/08/2027","18/08/2027","Sicilia",3500,"12435125")
    package_list.add_package(package4)
    assert search_destination_price(package_list,"Sicilia",4000) == [package4]
    assert search_destination_price(package_list,"Roma", 5000) == [package3]
    assert search_destination_price(package_list,"London",5000) == "No packages matched the search filters"

def test_search_finish_date():
    """
    Testing the search_finish_date() function
    :return: None
    """
    package_list = PackageList()
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package2 = Package("04/03/2027", "12/03/2027", "Roma", 4500, "18423252")
    package3 = Package("02/12/2026", "15/12/2026", "London", 3000, "13542414")
    package_list.set_package_list([package, package2, package3])
    assert search_finish_date(package_list,"15/12/2026") == [package, package3]
    assert search_finish_date(package_list,"12/03/2027") == [package2]
    assert search_finish_date(package_list,"01/12/2026") == "No packages matched the search filters"
    package4 = Package("11/08/2027","18/08/2027","Sicilia",3500,"12435125")
    package_list.add_package(package4)
    assert search_finish_date(package_list,"18/08/2027") == [package4]
    assert search_finish_date(package_list,"12/04/2027") == "No packages matched the search filters"

def test_search():
    """
    This function tests the entire search functionality
    :return: None
    """
    test_contains()
    test_search_interval()
    test_search_destination_price()
    test_search_finish_date()

