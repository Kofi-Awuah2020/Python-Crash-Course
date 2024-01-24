# input() Function
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

"""
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
"""
# Using a flag
active = True
while active:
    message = input(prompt)

    if message == 'quit': # Set flag to False to stop while loop
        active = False
    else:
        print(message)