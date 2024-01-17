current_users = ['sly', 'kong', 'sifu', 'rambo', 'lea']
new_users = ['rambo', 'reptile', 'jet li', 'sifu', 'raiden']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Username: {new_user} unavailable. Enter a new username.")
    else:
        print(f"Username: {new_user} available.")
    