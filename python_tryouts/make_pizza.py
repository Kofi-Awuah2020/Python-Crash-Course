# Passing an Arbitary Number of Arguments
# This would require variadic funcitons in C lol
def make_pizza(size, *toppings): # '*toppings' creates a tuple
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')