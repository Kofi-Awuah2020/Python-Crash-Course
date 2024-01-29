# Moving items from One List to Another

# Start with isers that need to be verfied,
# and an empty to hold confirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Veryfying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())