person_1 = {
    'first_name' : 'sam',
    'last_name' : 'fisher',
    'age' : 43,
    'city' : 'jakatar',
    }
person_2 = {
    'first_name' : 'jack',
    'last_name' : 'reacher',
    'age' : 35,
    'city' : 'chicago',
}
person_3 = {
    'first_name' : 'jack',
    'last_name'  : 'ryan',
    'age' : 37,
    'city' : 'washington DC',
}

action_stars = [person_1, person_2, person_3]

"""
print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())
"""

for stars in action_stars:
    print("\nPersonal details ...")
    for person_info, data in stars.items():
        print(f"{person_info.title()} : {data}")