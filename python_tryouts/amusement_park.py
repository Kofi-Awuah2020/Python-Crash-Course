# The if-elif-else Chain
age = 65
if age < 4:
    price = 0
elif 4 <= age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")