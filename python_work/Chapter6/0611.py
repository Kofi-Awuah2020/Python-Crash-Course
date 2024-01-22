cities = {
    'cairo' : {
        'country' : 'egypt',
        'population' : '109.3 million',
        'sights' : 'pyramids',
    },
    'accra' : {
        'country' : 'ghana',
        'population' : '30 million',
        'sights' : 'mole national park',
    },
    'dakar' : {
        'country' : 'senegal',
        'population' : '16.88 million',
        'sights' : 'the African Renaissance Monument'
    },
}
for city, fun_facts in cities.items():
    print(f"\n{city.title()}")
    for key, value in fun_facts.items():
        print(f"{key.title()} : {value}")