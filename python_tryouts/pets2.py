# Positional Arguments
def describe_pet(pet_name, animal_type='dog'): # Using a default value
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}")

describe_pet('hamster', 'harry')
describe_pet(pet_name='willie')

# Keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')

describe_pet()