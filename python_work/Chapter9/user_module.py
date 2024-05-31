"""A class representing a User"""

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
