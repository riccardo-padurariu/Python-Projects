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
        self.start_date = start_date

    def set_finish_date(self,date):
        self.finish_date = finish_date

    def set_destination(self, destination):
        self.destination = destination

    def set_price(self, price):
        self.price = price

packages = []