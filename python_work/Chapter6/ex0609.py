favourite_places = {
    'carl' : ['ibizza', 'hawai'],
    'hans' : ['paris', 'swiss alps'],
    'johnny' : ['egypt', 'jerusalem'],
}

for name, places in favourite_places.items():
    print(f"\n{name.title()}'s favourite places are: ")
    for place in places:
        print(f"\t{place.title()}") 