# Creating a Restuarant class
class Restuarant:
    """Modelling a Restuarant"""

    def __init__(self, restuarant_name, cusine_type):
        """Initialize restuarant name and cusine attribute"""
        self.name = restuarant_name
        self.cuisine = cusine_type

    def describe_restuarant(self):
        print(f"The restuarants name is {self.name}")
        print(f"The cusine we serve is {self.cuisine}")

    def open_restuarant(self):
        print(f"{self.name} is open")

restuarant = Restuarant('KFC', 'Spicy chicken bucket')

print(f"{restuarant.name} is my favourite restaurant.")
print(f"{restuarant.cuisine} is my favourite meal on the menu")

# my_restuarant