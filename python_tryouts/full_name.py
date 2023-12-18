# Combining the value of string variables - fstrings #
first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name} {last_name}" # Don't forget the char 'f' 
print(full_name.title())
print(f"Hello, {full_name.title()}!") # Don't forget the char 'f'

message = f"Hello, {full_name}!" #the 'f' is outside of the quotation marks
print(message)