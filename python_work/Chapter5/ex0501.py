# Conditional Tests
dogs = 'dobberman', 'german shepherd', 'american pitbull'
print("Is dog == 'dobberman'? I predict True")
print(dogs == 'dobberman')

print("\nIs dogs == 'german shepherd? I predict false")
print(dogs == 'german shepherd')

print(dogs == 'husky')
print(dogs != 'dobberman')
print(dogs == 'pitbull')
print(dogs != 'rottweiler')
print(dogs != 'dalmation')
print(dogs != 'bulldog')
print(dogs != 'Chiwawa')
print(dogs != 'Dragon')

# ex 0502
dog1  = 'Rotweiler'
if dog1 not in dogs:
    print("\nWe don't have that breed of dog")

dog2 = 'German Shepherd'
if dog2.lower() in dogs:
    print("We have that breed, but they are expensive")