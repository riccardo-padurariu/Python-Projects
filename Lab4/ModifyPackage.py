from PackageClass import Package, packages

def display_packages():
    """
    Displays the packages
    :return: None
    """
    for package in packages:
        print(package)

def exists(id):
    """
    Returns a tuple containing a boolean indicating whether or not the id paramater exists
    in the existing packages and the index of that package in the packages list, (False, -1) otherwise
    :param id: str
    :return: tuple(bool, int)
    """
    for index, package in enumerate(packages):
        if package.id == id:
            return True, index
    return False, -1

def get_selected_id(status):
    """
    Returns a tuple containing an existing id from the user and it's position in the packages list
    :param status: str
    :return: tuple(str, int)
    """
    id = input(f"Please enter the id you want to {status}: ")
    condition, index = exists(id)
    while not condition:
        id = input(f"The id must exist. Please enter again the id of the package you want to {status}: ")
        condition, index = exists(id)

    return id, index


def choose_option():
    """
    Gets a valid option for the user to modify the corresponding package
    :return: str
    """
    print("1. Start Date")
    print("2. Finish Date")
    print("3. Destination")
    print("4. Price")
    option = input("Choose the property you want to modify(from 1 to 4): ")

    while not option.isdigit() or (option.isdigit() and (int(option) < 1 or int(option) > 4)):
        option = input("The option must be an integer between 1 and 4. Please enter again: ")

    return option

def set_new_date(index, id, status, other_date = None):
    """
    Sets the start_date or finish_date(depends on the status) of the package corresponding
    to the id to a valid date got as input from the user. It uses the other_date if it's
    setting the finish_date, the other_date being the current start_date
    :param index: int
    :param id: str
    :param status: str
    :param other_date: str
    :return: None
    """
    print(f"You selected to modify the {status} date")
    date = (f"Please enter the new {status} date: ")
    condition, feedback = valid_date(date, other_date)
    while not condition:
        date = input(f"The {status} date must {feedback}. Please enter again the {status} date(dd/mm/yyyy): ")
        condition, feedback = valid_date(date, other_date)

    if status == "start":
        packages[index].set_start_date(date)
    elif status == "finish":
        packages[index].set_finish_date(date)
    print(f"Package {status} set to: {date}")

def set_destination(index, id):
    """
    Sets the destination of the package corresponding to the id parameter, destination got as input from the user
    :param index: int
    :param id: str
    :return: None
    """
    print("You selected to modify the destination property")
    destination = input("Please enter the new destination: ")
    while destination == "":
        destination = input("Enter a valid destination: ")

    packages[index].set_destination(destination.capitalize())
    print(f"Package destination set to: {destination}")

def set_price(index, id):
    """
    Sets the price of the package corresponding to the id parameter, price got as input from the user
    :param index: int
    :param id: str
    :return: None
    """
    print("You selected to modify the price property")
    price = input("Please enter the new price: ")
    while not price.isdigit() :
        price = input("The price must be a number. Please enter again: ")

    packages[index].set_price(price)
    print(f"Package price set to: {price}")

def modify_package():
    """
    The main function that implements the functionality of the modify package feature
    :return: None
    """
    if not packages:
        print("No tour packages available")
        return

    print("You selected option 2: modifying an existing tour package")
    exit = input("If you want to go back to the main menu, press 5, else press Enter: ")
    if exit == "5":
        return
    print("Those are the packages available:")
    display_packages()
    id, index = get_selected_id("modify")
    print(f"You selected the tour package with the Id {id}:")
    print(packages[index])

    option = choose_option()
    if option == "1":
        set_start_date(index, id)
    elif option == "2":
        set_finish_date(index, id, packages[index].start_date)
    elif option == "3":
        set_destination(index, id)
    elif option == "4":
        set_price(index, id)

    print("The package was modified successfully! Here is the updated version:")
    print(packages[index])