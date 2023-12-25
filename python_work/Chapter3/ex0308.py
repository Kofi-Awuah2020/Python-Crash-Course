# Sorting a List
bucket_list = ['Swiss Alps', 'Jerusalem', 'Bahamas', 'Hawai']
print(bucket_list) # Original Order

print(sorted(bucket_list)) # Sorting alphabetically temporarily
print(f"{bucket_list}\n") # The list is still unchanged

print(sorted(bucket_list, reverse=True)) #Sorting in reverse temporarily
print(f"{bucket_list}\n") # List still unchanged

bucket_list.reverse() #Reversing the list
print(bucket_list)
bucket_list.reverse() #Reverting the order
print(f"{bucket_list}\n")

bucket_list.sort() #Sorting the list permanently
print(bucket_list)
bucket_list.sort(reverse=True) #Sorting the list in reverse
print(bucket_list)