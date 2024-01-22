favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
}
poll_candidates = ['john', 'sarah', 'reeves', 'phil']
for name in favorite_languages.keys():
    if name in poll_candidates:
        print("Thank you for taking the poll")
    else:
        print("You are invited to take the poll")