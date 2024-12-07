def get_count_words(text: str) -> int:
    return len(text.split())

def get_character_frequency(text: str):
    char_frequency = {}
    
    for char in text.lower():
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    return char_frequency

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = get_count_words(file_contents)
    char_frequency = get_character_frequency(file_contents)
    print(f"{char_frequency}")