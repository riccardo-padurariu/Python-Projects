from domain import Package, PackageList

def test_getters():
    """
    Testing the getters from the Package class
    :return: None
    """
    package = Package("12/12/2026","15/12/2026","Paris",2500,"12412412")
    assert package.get_start_date() == "12/12/2026"
    assert package.get_finish_date() == "15/12/2026"
    assert package.get_destination() == "Paris"
    assert package.get_price() == 2500
    assert package.get_id() == "12412412"

def test_setters():
    """
    Testing the setters from the Package class
    :return: None
    """
    package = Package("11/11/2026","18/11/2026","London",3000,"13542414")
    package.set_start_date("05/11/2026")
    assert package.get_start_date() == "05/11/2026"
    package.set_finish_date("21/11/2026")
    assert package.get_finish_date() == "21/11/2026"
    package.set_destination("Roma")
    assert package.get_destination() == "Roma"
    package.set_price(2500)
    assert package.get_price() == 2500

def test_package_list_add_package():
    """
    Testing the add_package() method from the PackageList class
    :return: None
    """
    package_list = PackageList()
    assert package_list.get_package_list() == [] and package_list.get_package_list_history() == []
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package_list.add_package(package)
    assert package_list.get_package_list() == [package] and package_list.get_package_list_history() == [[]]
    package2 = Package("11/11/2026","18/11/2026","London",3000,"13542414")
    package_list.add_package(package2)
    assert package_list.get_package_list() == [package, package2] and package_list.get_package_list_history() == [[],[package]]
    package3 = Package("04/03/2027","12/03/2027","Roma",4500, "18423252")
    package_list.add_package(package3)
    assert package_list.get_package_list() == [package, package2, package3] and package_list.get_package_list_history() == [[],[package],[package, package2]]

def test_package_list_set_package_list():
    """
    Testing the set_package_list() method from the PackageList class
    :return: None
    """
    package_list = PackageList()
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package2 = Package("11/11/2026","18/11/2026","London",3000,"13542414")
    package3 = Package("04/03/2027","12/03/2027","Roma",4500, "18423252")
    assert package_list.get_package_list() == [] and package_list.get_package_list_history() == []
    package_list.set_package_list([package, package2, package3])
    assert package_list.get_package_list() == [package, package2, package3] and package_list.get_package_list_history() == [[]]
    package_list.set_package_list([package, package3])
    assert package_list.get_package_list() == [package, package3] and package_list.get_package_list_history() == [[], [package, package2, package3]]
    package_list.set_package_list([package2])
    assert package_list.get_package_list() == [package2] and package_list.get_package_list_history() == [[], [package, package2, package3], [package, package3]]

def test_package_list_exists_id():
    """
    Testing the exists_id() method from the PackageList class
    :return: None
    """
    package_list = PackageList()
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package2 = Package("11/11/2026", "18/11/2026", "London", 3000, "13542414")
    package3 = Package("04/03/2027", "12/03/2027", "Roma", 4500, "18423252")
    package_list.set_package_list([package, package2, package3])
    assert package_list.exists_id("13542414") == (True, 1)
    assert package_list.exists_id("19542314") == (False, -1)
    assert package_list.exists_id("18423252") == (True, 2)
    package4 = Package("12/04/2027", "20/04/2027", "Rio de Janeiro",4500,"02234414")
    package_list.add_package(package4)
    assert package_list.exists_id("96323351") == (False, -1)
    assert package_list.exists_id("02234414") == (True, 3)

def test_package_list_get_package():
    """
    Testing the get_package() method from the PackageList class
    :return: None
    """
    package_list = PackageList()
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package2 = Package("11/11/2026", "18/11/2026", "London", 3000, "13542414")
    package3 = Package("04/03/2027", "12/03/2027", "Roma", 4500, "18423252")
    package_list.set_package_list([package, package2, package3])
    assert package_list.get_package("12412412") == package
    assert package_list.get_package("12413212") is None
    package4 = Package("12/04/2027", "20/04/2027", "Rio de Janeiro",4500,"02234414")
    package_list.add_package(package4)
    assert package_list.get_package("02234414") == package4
    assert package_list.get_package("18423252") == package3

def test_package_list_set_attribute():
    """
    Testing the set_attribute() method from the PackageList class
    :return:
    """
    package_list = PackageList()
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package2 = Package("11/11/2026", "18/11/2026", "London", 3000, "13542414")
    package3 = Package("04/03/2027", "12/03/2027", "Roma", 4500, "18423252")
    package_list.set_package_list([package, package2, package3])
    package_list.set_package_attribute("12412412","destination","Cluj")
    assert package_list.get_package("12412412").get_destination() == "Cluj"
    package_list.set_package_attribute("18423252","start_date","01/12/2026")
    assert package_list.get_package("18423252").get_start_date() == "01/12/2026"
    package_list.set_package_attribute("13542414","price",4000)
    assert package_list.get_package("13542414").get_price() == 4000

def test_package_list_undo_operation():
    """
    Testing the undo_operation() method from the PackageList function
    :return: None
    """
    package_list = PackageList()
    package = Package("12/12/2026", "15/12/2026", "Paris", 2500, "12412412")
    package2 = Package("11/11/2026", "18/11/2026", "London", 3000, "13542414")
    package3 = Package("04/03/2027", "12/03/2027", "Roma", 4500, "18423252")
    package_list.add_package(package)
    assert package_list.get_package_list() == [package] and package_list.get_package_list_history() == [[]]
    package_list.undo_operation()
    assert package_list.get_package_list() == [] and package_list.get_package_list_history() == []
    package_list.set_package_list([package2,package3])
    package_list.add_package(package)
    package_list.undo_operation()
    assert package_list.get_package_list() == [package2, package3] and package_list.get_package_list_history() == [[]]
    package_list.undo_operation()
    package_list.undo_operation()
    assert package_list.get_package_list() == [] and package_list.get_package_list_history() == []


def test_domain():
    """
    This function tests the entire domain methods
    :return: None
    """
    test_getters()
    test_setters()
    test_package_list_add_package()
    test_package_list_set_package_list()
    test_package_list_exists_id()
    test_package_list_get_package()
    test_package_list_set_attribute()
    test_package_list_undo_operation()