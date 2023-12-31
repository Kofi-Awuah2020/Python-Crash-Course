# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:] # Producing a seperate list
                            # You would have to use a for loop in C
                            # Dont forget '[:]'
# This doesn't work as intended:
# friends_foods = my_foods

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favourite foods are:")
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favourite foods are:")
for friend_food in friends_foods:
    print(friend_food)

