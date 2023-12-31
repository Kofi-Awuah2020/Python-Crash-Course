# Defining a Tuple
dimensions = (200, 50) #The commas is neccessay when defining a tuple
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250 #This synatx leads to an error

#Looping Through All values in a Tuple
for dimension in dimensions:
    print(dimension)

#Writing Over a Tuple
print("Orginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)