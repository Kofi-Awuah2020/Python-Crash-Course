# Using Lists
guest_list = ['Moses', 'David', 'Samson', 'Adam', 'Noah', 'Abraham']
invitation_msg = "I would love to have you over for dinner"
print(f"{guest_list[0]}, {invitation_msg}")
print(f"{guest_list[1]}, {invitation_msg}")
print(f"{guest_list[2]}, {invitation_msg}")
print(f"{guest_list[3]}, {invitation_msg}")
print(f"{guest_list[4]}, {invitation_msg}")
print(f"{guest_list[5]}, {invitation_msg}")

#ex0305
print(f"\nSorry guys, {guest_list[2]} can't find his way here")
print("I forgot the Philisines took out his eyes lol\n")

guest_list.remove('Samson')
guest_list.insert(2, 'Eve')
second_invitation = "These are the new invites for everyone who will make it"
print(f"{guest_list[0]}, {second_invitation}")
print(f"{guest_list[1]}, {second_invitation}")
print(f"{guest_list[2]}, {second_invitation}")
print(f"{guest_list[3]}, {second_invitation}")
print(f"{guest_list[4]}, {second_invitation}")
print(f"{guest_list[-1]}, {second_invitation}")

# ex0306
print("\nGuess What! I found a bigger table!! Isn't that great!!!")
guest_list.insert(0, 'Job')
guest_list.insert(3, 'Ezekiel')
guest_list.append('John')

third_invitation = "again this is newer invite"
print(f"{guest_list[0]}, {third_invitation}")
print(f"{guest_list[1]}, {third_invitation}")
print(f"{guest_list[2]}, {third_invitation}")
print(f"{guest_list[3]}, {third_invitation}")
print(f"{guest_list[4]}, {third_invitation}")
print(f"{guest_list[5]}, {third_invitation}")
print(f"{guest_list[6]}, {third_invitation}")
print(f"{guest_list[7]}, {third_invitation}")
print(f"{guest_list[8]}, {third_invitation}")

# ex0307
print("\nBad news guys and gal, the bigger table was a false alarm")
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()

final_invite = "this is the last invite"
print(f"{guest_list[0]}, {final_invite}")
print(f"{guest_list[1]}, {final_invite}")

del guest_list[0]
del guest_list[0]

print(guest_list)
print(f"There are only {len(guest_list)} guests left")