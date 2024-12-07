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

def print_report(file_path: str, word_count: str, char_count: dict):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    alpha_chars = "abcdefghijklmnopqrstuvwxyz"
    
    for k in char_count:
        if k in alpha_chars:
            frequency = char_count[k]
            print(f"The '{k}' chracter was found {frequency} times")

def get_file_contents(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    file_path = "books/frankenstein.txt"

    file_contents = get_file_contents(file_path)
    word_count = get_count_words(file_contents)
    char_frequency = get_character_frequency(file_contents)
    
    print_report(file_path, word_count, char_frequency)

if __name__ == "__main__":
    main()