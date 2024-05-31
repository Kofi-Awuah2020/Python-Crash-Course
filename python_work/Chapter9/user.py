"""A set of classes representing an Admin and a User"""

class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Details: \nFirst Name: {self.first_name}")
        print(f"Last Name: {self.last_name} \nAge: {self.age}")

    def greet_user(self):
        fullname = self.first_name + " " + self.last_name
        print(f"Hello {fullname}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def rest_login_attempts(self):
        self.login_attempts = 0

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
