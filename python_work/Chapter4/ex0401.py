# Working with For Loops
pizzas = ['crisbreezy', 'kessame', 'chicken pepproni']
for pizza in pizzas:
    print(f"I love the {pizza} pizza, heaven to my taste buds\n")

print("I just love pizza") #This statement is lie lol

#ex 411
friend_pizza = pizzas[:]

pizzas.append('pinapple')
friend_pizza.append('vegan')

for pizza in pizzas:
    print(f"My favourite pizzas are: {pizzas}")
for friend in friend_pizza:
    print(f"My friend's favourite pizzas are: {friend_pizza}")