# SLicing a List
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3])#Remember off by one

print(players[1:4]) #prints 1st 2nd 3rd element

print(players[:4]) #prints from the first index to the third index

print(players[2:]) #prints third index to the end of the list

print(players[-3:]) #prints last three elements in the list

print(players[0::2]) # Third vvalue tells Python to skip how many items

# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())