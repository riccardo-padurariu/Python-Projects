from domain import Package, PackageList
from crud_business import delete_destination, count_days, exists_destination, delete_days, valid_date
from search_packages_business import contains

# Tests for the testable functions

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

def test_count_days():
    """
    Testing the count_days() function
    :return: None
    """
    assert count_days("12/12/2026","17/01/2027") == 37
    assert count_days("11/11/2026","18/11/2026") == 8
    assert count_days("14/02/2027","20/02/2027") == 7
    assert count_days("07/06/2027","14/07/2027") == 38
    assert count_days("24/05/2027","11/11/2027") == 172

def test_delete_destination():
    """
    Testing the delete_destination() function
    :return: None
    """
    assert delete_destination(
        PackageList([
            Package("12/12/2026", "15/12/2026", "Paris", "3000", "12355261"),
            Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
            Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
            Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
            Package("12/04/2027", "18/04/2027", "Ibiza", "5200", "38163496")],
        [[]]),
        "Paris") == ["41235113", "23959873", "38163496"]
    assert delete_destination(
        PackageList([
            Package("15/12/2026", "19/12/2026", "Canada", "3050", "72252463"),
            Package("11/11/2026", "18/11/2026", "Zimbawe", "2800", "13463571"),
            Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
            Package("20/01/2027", "28/01/2027", "Canada", "4500", "13743521"),
            Package("14/02/2027", "24/02/2027", "Rio de Janeiro", "5200", "16346134")],
        [[]]),
        "Canada") == ["13463571", "12455242", "16346134"]
    assert delete_destination(
        PackageList([
            Package("23/10/2026", "31/10/2026", "Oslo", "3000", "12492353"),
            Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
            Package("07/06/2027", "14/07/2027", "Paris", "3500", "12423461"),
            Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
            Package("12/04/2027", "18/04/2027", "Oslo", "5200", "38163496")],
        [[]]),
        "Oslo") == ["41235113", "12423461", "23959873"]
    assert delete_destination(
        PackageList([
            Package("12/12/2026", "15/12/2026", "Tenerife", "3000", "12355261"),
            Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
            Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
            Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
            Package("12/04/2027", "18/04/2027", "Tenerife", "5200", "38163496")],
        [[]]),
        "Tenerife") == ["41235113", "12455242"]

def test_delete_days():
    """
    Testing the delete_days function
    :return: None
    """
    assert delete_days(
        PackageList([
            Package("12/12/2026", "15/12/2026", "Paris", "3000", "12355261"),
            Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
            Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
            Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
            Package("12/04/2027", "18/04/2027", "Ibiza", "5200", "38163496")],
        [[]]),
        5) == ['41235113', '12455242', '23959873', '38163496']
    assert delete_days(
        PackageList([
            Package("15/12/2026", "19/12/2026", "Canada", "3050", "72252463"),
            Package("11/11/2026", "18/11/2026", "Zimbawe", "2800", "13463571"),
            Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
            Package("20/01/2027", "28/01/2027", "Canada", "4500", "13743521"),
            Package("14/02/2027", "24/02/2027", "Rio de Janeiro", "5200", "16346134")],
        [[]]),
        10) == ['12455242', '16346134']
    assert delete_days(
        PackageList(
        [
            Package("23/10/2026", "31/10/2026", "Oslo", "3000", "12492353"),
            Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
            Package("07/06/2027", "14/07/2027", "Paris", "3500", "12423461"),
            Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
            Package("12/04/2027", "18/04/2027", "Oslo", "5200", "38163496")],
        [[]]),
        3) == ['12492353', '41235113', '12423461', '23959873', '38163496']
    assert delete_days(PackageList(
        [
            Package("12/12/2026", "15/12/2026", "Tenerife", "3000", "12355261"),
            Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
            Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
            Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
            Package("12/04/2027", "18/04/2027", "Tenerife", "5200", "38163496")],
        [[]]),
        7) == ['41235113', '12455242', '23959873', '38163496']


def test_exists_destination():
    """
    Testing the exists_destination function
    :return: None
    """
    assert exists_destination(PackageList(
        [
            Package("12/12/2026", "15/12/2026", "Paris", "3000", "12355261"),
            Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
            Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
            Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
            Package("12/04/2027", "18/04/2027", "Ibiza", "5200", "38163496")],
        [[]]),
        "Paris") == True
    assert exists_destination(PackageList(
        [
            Package("15/12/2026", "19/12/2026", "Canada", "3050", "72252463"),
            Package("11/11/2026", "18/11/2026", "Zimbawe", "2800", "13463571"),
            Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
            Package("20/01/2027", "28/01/2027", "Canada", "4500", "13743521"),
            Package("14/02/2027", "24/02/2027", "Rio de Janeiro", "5200", "16346134")],
        [[]]),
        "Canada") == True
    assert exists_destination(PackageList(
        [
            Package("23/10/2026", "31/10/2026", "Oslo", "3000", "12492353"),
            Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
            Package("07/06/2027", "14/07/2027", "Paris", "3500", "12423461"),
            Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
            Package("12/04/2027", "18/04/2027", "Oslo", "5200", "38163496")],
        [[]]),
        "London") == False
    assert exists_destination(PackageList(
        [
            Package("12/12/2026", "15/12/2026", "Tenerife", "3000", "12355261"),
            Package("11/11/2026", "18/11/2026", "Roma", "3200", "41235113"),
            Package("13/12/2026", "23/12/2026", "Paris", "3500", "12455242"),
            Package("11/11/2026", "18/11/2026", "Tenerife", "4500", "23959873"),
            Package("12/04/2027", "18/04/2027", "Tenerife", "5200", "38163496")],
        [[]]),
        "Tenerife") == True


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