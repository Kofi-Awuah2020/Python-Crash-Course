prompt = "\nWhat is your age? "

age = input(prompt)
age = int(age)

active = True
while active:
    if age < 3:
        print("The ticket is free.")
        break
    elif age <= 12:
        print("The ticket is $10.")
        break
    elif age > 12:
        print("The ticket is $15.")
        break