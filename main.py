from stats import count_words, count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    text = get_book_text("books/frankenstein.txt")
    print("Analyzing book found at books/frankenstein.txt...")
    num_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    letter_count = dict(sorted(count_letters(text).items(), key=lambda item: item[1], reverse=True))
    print("--------- Character Count -------")
    for key, value in letter_count.items():
        print(f"{key}: {value}")

main()