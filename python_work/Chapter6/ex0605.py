rivers = {
    'nile' : 'egypt',
    'volta' : 'ghana',
    'amazon' : 'brazil',
}
for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}")
print("\n")
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())