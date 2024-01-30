def city_country(city, country):
    formatted_string = f"{city.title()}, {country.title()}"
    return formatted_string

destination = city_country('kumasi', 'Ghana')
print(destination)

destination = city_country('accra', 'Ghana')
print(destination)

destination = city_country('juarez', 'mexico')
print(destination)