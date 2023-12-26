# Using range() to Make a List of Numbers
'''
squares = []
for value in range(1, 11): #store range 1 - 10 inclusive in value
    square = value ** 2 #square value and store in variable square
    squares.append(square) #append result to the squares list

print(squares)

# Writing the code concisely
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)
'''
#List Comprehension
squares = [value ** 2 for value in range(1, 11)]
print(squares)