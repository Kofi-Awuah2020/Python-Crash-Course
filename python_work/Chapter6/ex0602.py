favourite_numbers = {
    'alice' : [9 , 10],
    'marvin' : [3, 6],
    'reacher' : [0, 3],
    'jordan' : [23, 1],
    'bond' : [7 , 11],
}
"""
print(f"Alice's favourite number is : {favourite_numbers['alice']}")
print(f"Marvin's favourite number is : {favourite_numbers['marvin']}")
print(f"Reacher's favourite number is : {favourite_numbers['reacher']}")
print(f"Jordan's favourite number is : {favourite_numbers['jordan']}")
print(f"Bond's favourite number is : {favourite_numbers['bond']}")
"""
for names, numbers in favourite_numbers.items():
    print(f"{names.title()}'s favourite numbers are: ", end="")
    for number in numbers:
        print(f"{number}", end=", ")
    print("\n")