sandwich_orders = ['p & j', 'egg', 'pastrami', 'tuna', 'pastrami', 'vegan', 'pastrami', 'avocado']
finished_sandwich = []
print("The deli has run out of pastrami sandwich!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"\nI made you a {sandwich_order} sandwich.")

    finished_sandwich.append(sandwich_order)
for sandwich in finished_sandwich:
    print(f"\nThe {sandwich} sandwich was made.")