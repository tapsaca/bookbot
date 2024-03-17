def count_letters(text: str):
    letter_count = {}
    for character in text:
        if character.isalpha():
            lowered = character.lower()
            if lowered in letter_count:
                letter_count[lowered] += 1
            else:
                letter_count[lowered] = 1
    return letter_count

def count_words(text: str):
    return len(text.split())

def get_text_from_file(path: str):
    with open(path) as f:
        return f.read()

def main():
    path = input("Relative path to the text: ")
    try:
        text = get_text_from_file(path)
    except FileNotFoundError:
        print("File not found")
        return
    print()
    print(f"--- Begin report of {path} ---")
    print(f"Number of words in text: {count_words(text)}")
    print()
    letter_count = dict(sorted(count_letters(text).items(), key=lambda item: item[1], reverse=True))
    for key, value in letter_count.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

main()