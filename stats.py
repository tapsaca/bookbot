def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_count = {}
    for character in text:
        if character.isalpha():
            lower_case_letter = character.lower()
            if lower_case_letter not in letter_count:
                letter_count[lower_case_letter] = 0
            letter_count[lower_case_letter] += 1
    return letter_count