from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
contents = contents.replace('python', 'C')
print(f"{contents}\n")

lines = contents.splitlines()
for line in lines:
    print(line)