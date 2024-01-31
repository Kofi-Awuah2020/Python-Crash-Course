# Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info): # '**user_info' creates a dictionary
    """Build a dictionary containing everything we know about a user."""
    user_info['first'] = first
    user_info['last'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)