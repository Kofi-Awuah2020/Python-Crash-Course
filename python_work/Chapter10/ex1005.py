from pathlib import Path

path = Path('guest_book.txt')

print("Press 's' to quit!")
content = ''
while True:
    name = input("What is your name? ")
    if name == 's':
        break
    content += f"{name}\n" 

path.write_text(content)