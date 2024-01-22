favourite_languages = {
    'jen' : 'python', 
    'sarah' : 'c', 
    'edward' : 'rust', 
    'phil' : 'python',
    }

language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

# Looping Through All the Keys in a Dictionary
for name in favourite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")

# Looping Through a Dictionary's Keys in a Particluar Order
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping Through All Values in a Dictionary
print("\nThe following languages have been mentioned:")
for language in favourite_languages.values():
    if language == 'python':
        print(f"{language.title()} is the best language")
    else:
        print(language.title())

# Using the 'set()' function
for language in set(favourite_languages.values()):
    print(f"\n{language.title()}")

# Nesting a List in a Dictionary.
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is", end=" ")
        for language in languages:
            print(language.title())