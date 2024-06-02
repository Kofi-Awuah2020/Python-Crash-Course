from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working data.\n"

path = Path('programming.txt')
path.write_text(contents)