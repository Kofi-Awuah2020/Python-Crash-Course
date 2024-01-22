pet_1 = {
    'animal' : 'penguin',
    'owner' : 'carl',
}
pet_2 = {
    'animal' : 'cat',
    'owner' : 'hans',
}
pet_3 = {
    'animal' : 'koi fish',
    'owner' : 'hanzo',
}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print("\nPet Details ...")
    for key, value in pet.items():
        print(f"{key.title()} : {value.title()}")