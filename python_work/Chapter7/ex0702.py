dinner_group = input("How many people are in the dinner group? ")
dinner_group = int(dinner_group)

if dinner_group > 8:
    print("Sorry, you will have to wait for a table.")
else:
    print("Right this way, your table is ready.")