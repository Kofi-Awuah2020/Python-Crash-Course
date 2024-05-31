import user  # ignore: type

john_doe = user.Administrator('John', 'Doe', 45)
john_doe.privilages.show_privilages(["can delete post", "can add post"])