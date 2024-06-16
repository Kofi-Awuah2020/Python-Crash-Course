# A programme that reads the contents of a file and prints it
from pathlib import Path

def print_files(path):
    try:
        content = path.read_text()
    except FileNotFoundError:
        print("The file cannot be found")
    else:
        print(content)

filenames = ['dogs.txt', 'cats.txt']
for index, filename in enumerate(filenames):
    path = Path(filename)
    print_files(path)
    if index < len(filenames) - 1:
        print()