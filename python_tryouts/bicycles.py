# Using lists #
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) #This would cause an error in C lol

# Accessing an element in a list via index #
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1]) # Acessing the last element in a list

# Creating a message with an individual value in a list #
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)