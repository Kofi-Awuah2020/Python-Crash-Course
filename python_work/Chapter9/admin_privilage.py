"""A set of classes modelling an Admin and admin privilages"""

from user_module import User # ignore: type

class Privilages:
    """Modelling a Privilages Class"""
    def __init__(self):
        self.privilages = []

    def show_privilages(self, admin_privilages):
        self.privilages = admin_privilages
        for privilage in self.privilages:
            print(privilage)

class Administrator(User):
    """Modelling an Administrator Class"""

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privilages = Privilages()
