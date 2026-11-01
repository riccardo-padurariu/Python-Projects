class Package():
    def __init__(self,start_date, finish_date, destination, price, id):
        self.start_date = start_date
        self.finish_date = finish_date
        self.destination = destination
        self.price = price
        self.id = id

    def __str__(self):
        return f"""
    Destination: {self.destination}
        From {self.start_date} to {self.finish_date}
        Price: {self.price}€
        Id: {self.id}"""

    def set_start_date(self,date):
        self.start_date = date

    def set_finish_date(self,date):
        self.finish_date = date

    def set_destination(self, destination):
        self.destination = destination

    def set_price(self, price):
        self.price = price

    def get_start_date(self):
        return self.start_date

    def get_finish_date(self):
        return self.finish_date

    def get_destination(self):
        return self.destination

    def get_price(self):
        return self.price

    def get_id(self):
        return self.id

class PackageList:
    def __init__(self, package_list = None, package_history = None):
        self.package_list = {
            "list": [] if package_list is None else package_list,
            "history": [] if package_history is None else package_history
        }

    def __str__(self):
        return f"""Package List:
        List: {self.package_list["list"]}
        History: {self.package_list["history"]} 
        """

    def update_history(self):
        new_package_list = []
        for package in self.package_list["list"]:
            new_package_list.append(package)
        self.package_list["history"].append(new_package_list)

    def exists_id(self, package_id):
        for index, package in enumerate(self.package_list["list"]):
            if package.id == package_id:
                return True, index

        return False, -1

    def add_package(self, package):
        self.update_history()
        self.package_list["list"].append(package)

    def set_package_list(self, new_package_list, delete = False, undo = False):
        if not delete and not undo:
            self.update_history()
            self.package_list["list"] = new_package_list.copy()
        else:
            self.package_list["list"] = new_package_list.copy()

    def set_package(self, package_id, new_package):
        for index, package in enumerate(self.package_list["list"]):
            if package.id == package_id:
                self.package_list["list"][index] = new_package
                self.update_history()
                return True
        return False

    def set_package_attribute(self, package_id, attribute, value):
        exists, index = self.exists_id(package_id)
        new_package = None
        current_package = self.get_package(package_id)
        if exists:
            match attribute:
                case "start_date":
                    #self.package_list["list"][index].set_start_date(value)
                    new_package = Package(value,
                                          current_package.get_finish_date(),
                                          current_package.get_destination(),
                                          current_package.get_price(),
                                          current_package.get_id())
                case "finish_date":
                    #self.package_list["list"][index].set_finish_date(value)
                    new_package = Package(current_package.get_start_date(),
                                  value,
                                  current_package.get_destination(),
                                  current_package.get_price(),
                                  current_package.get_id())
                case "destination":
                    #self.package_list["list"][index].set_destination(value)
                    new_package = Package(current_package.get_start_date(),
                                  current_package.get_finish_date(),
                                  value,
                                  current_package.get_price(),
                                  current_package.get_id())
                case "price":
                    #self.package_list["list"][index].set_price(value)
                    new_package = Package(current_package.get_start_date(),
                                  current_package.get_finish_date(),
                                  current_package.get_destination(),
                                  value,
                                  current_package.get_id())
                case _: return False

            self.package_list["list"][index] = new_package

            return True
        else:
            return False

    def get_package_list(self):
        return self.package_list["list"]

    def get_package_list_history(self):
        return self.package_list["history"]

    def get_package(self, id):
        for package in self.package_list["list"]:
            if package.id == id:
                return package

        return None

    def undo_operation(self):
        if len(self.package_list["history"]) > 0:
            self.set_package_list(self.package_list["history"].pop(), False, True)
            return True
        return False


