prompt = "\nEnter your choice toppings "
prompt += "\ntype 'quit' to exit: "

active = True
while active:
    topping = input(prompt)

    if topping == "quit":
        active = False
    else:
        print(f"Adding {topping} to the pizza")