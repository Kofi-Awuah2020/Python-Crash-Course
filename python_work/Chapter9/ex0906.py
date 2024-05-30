# EX0906

class Restuarant:
    """Modelling a Restuarant"""

    def __init__(self, restuarant_name, cusine_type):
        """Initialize restuarant name and cusine attribute"""
        self.name = restuarant_name
        self.cuisine = cusine_type
        self.number_served = 0

    def describe_restuarant(self):
        print(f"The restuarants name is {self.name}")
        print(f"The cusine we serve is {self.cuisine}")

    def open_restuarant(self):
        print(f"{self.name} is open")

    def set_number_served(self, customers_served):
        self.number_served = customers_served

    def increment_number_served(self, customers):
        self.number_served += customers

class IceCreamStand(Restuarant):
    """Modelling an Ice cream stand"""

    def __init__(self, restuarant_name, cusine_type):
        super().__init__(restuarant_name, cusine_type)
        self.flavours = []

    def display_flavours(self, ice_cream_flavours):
        self.flavours = ice_cream_flavours
    
        for flavour in self.flavours:
            print(flavour)

Best_icecream = IceCreamStand('Best', 'Nachos')
Best_icecream.display_flavours(['Chocolate', 'Vanilla', 'Strawberry'])