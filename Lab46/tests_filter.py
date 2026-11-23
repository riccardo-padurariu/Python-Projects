from domain import PackageList, Package
from filter_package_business import filter_destination_price, filter_month


def test_filter_destination_price():
    """
    Testing the filter_destination_price() function
    :return: None
    """
    package_list = PackageList()
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package2 = Package("11/11/2026", "18/11/2026", "Paris", 3000, "13542414")
    package3 = Package("04/03/2027", "12/03/2027", "Roma", 4500, "18423252")
    package_list.set_package_list([package, package2, package3])
    assert filter_destination_price(package_list,2700,"Paris") == [package, package2]
    package_list.add_package(package3)
    assert filter_destination_price(package_list,2000,"Roma") == [package3]
    assert filter_destination_price(package_list,4000,"Sicilia") == []
    package4 = Package("01/12/2026", "10/12/2026", "Roma", 4500, "19423652")
    package_list.set_package_list([package, package2, package3, package4])
    assert filter_destination_price(package_list,5000,"Roma") == [package, package2, package3, package4]
    assert filter_destination_price(package_list,4000,"Paris") == [package, package2]
    assert filter_destination_price(package_list,2200,"London") == []

def test_filter_month():
    """
    Testing the filter_month() function
    :return: None
    """
    package_list = PackageList()
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package2 = Package("11/11/2026", "18/11/2026", "Paris", 3000, "13542414")
    package3 = Package("04/03/2027", "12/03/2027", "Roma", 4500, "18423252")
    package_list.set_package_list([package, package2, package3])
    assert filter_month(package_list,"december") == [package2, package3]
    assert filter_month(package_list,"november") == [package3]
    assert filter_month(package_list,"march") == []
    package4 = Package("01/12/2026", "10/12/2026", "Roma", 4500, "19423652")
    package_list.set_package_list([package, package2, package3, package4])
    assert filter_month(package_list,"november") == [package, package3, package4]
    assert filter_month(package_list,"march") == [package, package4]
    assert filter_month(package_list,"december") == []


def test_filter():
    """
    This function tests the entire filter feature functions
    :return: None
    """
    test_filter_destination_price()
    test_filter_month()