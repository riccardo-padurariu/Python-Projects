from PackageClass import Package
from DeletePackages import delete_destination
from AddPackage import valid_date
from DeletePackages import count_days

# Tests for the testable functions

def test_count_days():
    """
    Testing the count_days() function
    :return: None
    """
    assert count_days("12/12/2026","17/01/2027") == 0

def test_delete_destination():
    """
    Testing the delete_destination() function
    :return: None
    """
    assert delete_destination([
    Package("12/12/2026", "15/12/2026", "Paris", "3000", "12355261"),
    Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
    Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
    Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
    Package("12/04/2027", "18/04/2027", "Ibiza", "5200", "38163496")],
    "Paris") == ["41235113", "23959873", "38163496"]
    assert delete_destination([
    Package("15/12/2026", "19/12/2026", "Canada", "3050", "72252463"),
    Package("11/11/2026", "18/11/2026", "Zimbawe", "2800", "13463571"),
    Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
    Package("20/01/2027", "28/01/2027", "Canada", "4500", "13743521"),
    Package("14/02/2027", "24/02/2027", "Rio de Janeiro", "5200", "16346134")],
    "Canada") == ["13463571", "12455242", "16346134"]
    assert delete_destination([
    Package("23/10/2026", "31/10/2026", "Oslo", "3000", "12492353"),
    Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
    Package("07/06/2027", "14/07/2027", "Paris", "3500", "12423461"),
    Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
    Package("12/04/2027", "18/04/2027", "Oslo", "5200", "38163496")],
    "Oslo") == ["41235113", "12423461", "23959873"]
    assert delete_destination([
    Package("12/12/2026", "15/12/2026", "Tenerife", "3000", "12355261"),
    Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
    Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
    Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
    Package("12/04/2027", "18/04/2027", "Tenerife", "5200", "38163496")],
    "Tenerife") == ["41235113", "12455242"]

def test_valid_date():
    """
    Testing the valid_date() function
    :return: None
    """
    assert valid_date("12/04/12e1") == (False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers")
    assert valid_date("17/07/2026") == (False, "be after the current date")
    assert valid_date("31/10/2026") == (True, "")
    assert valid_date("12/21/2026") == (False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers")
    assert valid_date("12/12/202") == (False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers")
    assert valid_date("/04/2002","12/01/2027") == (False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers")
    assert valid_date("25/12/2026") == (True, "")
    assert valid_date("") == (False, "match the pattern dd/mm/yyyy, where dd,mm and yyyy must be valid integers")