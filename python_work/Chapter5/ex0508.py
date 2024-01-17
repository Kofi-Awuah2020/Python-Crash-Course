usernames = ['king', 'jordan', 'rudy', 'pinger', 'admin']

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"\nHello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find users!")