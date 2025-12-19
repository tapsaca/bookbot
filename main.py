import sys
from stats import count_words, count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    print(f"Analyzing book found at {filepath}")
    num_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    letter_count = dict(sorted(count_letters(text).items(), key=lambda item: item[1], reverse=True))
    print("--------- Character Count -------")
    for key, value in letter_count.items():
        print(f"{key}: {value}")

main()