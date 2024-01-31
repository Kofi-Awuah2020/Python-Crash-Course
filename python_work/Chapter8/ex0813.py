def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first'] = first.title()
    user_info['last'] = last.title()
    return user_info

my_profile = build_profile("kofi", 'awuah', occupation='unemployed', status='married?', feeling='tired')
print(my_profile)