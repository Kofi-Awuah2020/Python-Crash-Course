from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
contents = contents.replace('python', 'C')
print(f"{contents}\n")

for line in contents.splitlines():
    print(line)