from pathlib import Path

def count_words(path):
    content = path.read_text()
    word_count = content.lower().count('the ')
    print(f"The word 'the' appears {word_count} number of times")

path = Path('gutenburg.txt')
count_words(path)