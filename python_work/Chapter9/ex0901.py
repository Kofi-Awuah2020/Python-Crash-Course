# Creating a Restuarant class
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


restuarant = Restuarant('KFC', 'Spicy chicken bucket')
new_restuarant = Restuarant('Barcelos', 'Family meal')
old_restuarant = Restuarant('Tasty Queen', 'Jollof')
his_restuarant = Restuarant('Oldies', 'Fufu')

print(f"{restuarant.name} is my favourite restaurant.")
print(f"{restuarant.cuisine} is my favourite meal on the menu")

new_restuarant.describe_restuarant()

old_restuarant.describe_restuarant()

his_restuarant.describe_restuarant()

# Exercise 0904
print(f"\nNumber of customers served: {restuarant.number_served}")

restuarant.set_number_served(12)
print(f"\nNumber of customers served: {restuarant.number_served}")

restuarant.increment_number_served(10)
print(f"\nNumber of customers served: {restuarant.number_served}")