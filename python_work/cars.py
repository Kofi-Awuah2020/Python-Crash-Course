# Sorting a List Permanently with the sort() method
cars = ['bmw', 'audi', 'toyato', 'subaru']
cars.sort() # List cannot be reverted to original order
print(cars) # List sorted to in alphabetical order

# Sorting a List in Reverse order Permanently
sneakers = ['nike', 'reeboks', 'jordans', 'adidaas']
sneakers.sort(reverse=True)
print(f"\n{sneakers}")

# Sorting a List Temporarily with the sorted() function
fruits = {'mango', 'guava', 'pineapples', 'strawberry'}
print("\nHere is the original list:")
print(fruits)

print("\nHere is the sorted list:")
print(sorted(fruits))

print("\nHere is the original list again:")
print(fruits)

# Printing a List in Reverse Order
horses = ['bruno', 'biggie', 'daisy', 'bucky']
print("\nOrginal List:")
print(horses)

horses.reverse()
print("\nList in reverse order")
print(horses)

# Finding the Length of a List
dogs = ['django', 'peace', 'biggie', 'black']
print(len(dogs))
