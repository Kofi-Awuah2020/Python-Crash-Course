def make_car(name, model, **car_info):
    car_info['car name'] = name
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)