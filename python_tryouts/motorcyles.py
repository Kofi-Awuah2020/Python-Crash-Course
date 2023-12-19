# Modyfing Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Changing a list's value using indexing
motorcycles[0] = 'ducati'
print(motorcycles)

# Appending to the end of a list
motorcycles.append('bmw')
print(motorcycles)

# Dynamically Building a List
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(f"\n{motorcycles}")

# Inserting Elements into a list
motorcycles.insert(0, 'ducati') # index followed by value
print(motorcycles)

# Removing Elements from a list
del motorcycles[0] # del comes before list name
print(f"\n{motorcycles}") #value cannot be accessed after del statement

# Removing an Item Using the pop() Method
popped_motorcycle = motorcycles.pop()
print("\n")
print(motorcycles)
print(popped_motorcycle)

# Printing a statement using the pop() Method
last_owned = popped_motorcycle
print(f"The last motorcycle I owned was a {last_owned.title()}")

# Popping Items from Any Position in a list
first_owned = motorcycles.pop(0)
print(f"The first motocycle I owned was a {first_owned.title()}.")

# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

#motorcycles.remove('ducati')
#print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")