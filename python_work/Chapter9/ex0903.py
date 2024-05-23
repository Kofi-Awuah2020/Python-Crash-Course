# Creating a User Class
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

user1 = User('John', 'Doe', 18)
user2 = User('King', 'Kong', 23)
user3 = User('Drew', 'Jackson', 25)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

new_user = User('Steve', 'Clark', 27)
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print(f"Login attempts: {new_user.login_attempts}")
new_user.rest_login_attempts()
print(f"Login attempts: {new_user.login_attempts}")