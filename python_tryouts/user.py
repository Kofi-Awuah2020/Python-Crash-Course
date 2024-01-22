# Looping Through a Dictionary
# Looping Through All Key-Value Pairs

user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi'
}

for key, value in user_0.items(): # items() method returns a sequence of key-value pairs
    print(f"\nKey: {key}")
    print(f"Value: {value}")