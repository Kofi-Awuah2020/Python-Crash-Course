"""Modelling a Lottery"""

from random import sample


def generate_ticket(ticket_pool, num_choices):
    """Generating a random ticket from the ticket pool"""
    return sample(ticket_pool, num_choices)

def main():
    ticket_pool = (23, 56, 'B', 'A', 'Z', 97, 'Q', 12, 35, 1, 7, 41, 37, 74)
    my_ticket = [7, 'Z', 'A', 41]
    winning_ticket = generate_ticket(ticket_pool, 4)
    count = 0

    while my_ticket != winning_ticket:
        winning_ticket = generate_ticket(ticket_pool, 4)
        count += 1 
    
    print(f"The loop ran {count} times before I won.")


if __name__ == '__main__':
    main()