# Create an empty dictionary
responses = {}

name = input("What is your name? ")
response = input("If you could visit one place in the world, where would you go? ")

responses[name] = response

print(f"{name.title()} would love to visit{response.title()}")