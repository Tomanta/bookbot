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

def convert_to_list(dict):
    converted_list = []
    for k in dict:
        converted_list.append({"char": k, "frequency": dict[k]})
    return converted_list

def print_report(file_path: str, word_count: str, char_count: dict):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    
    char_count_list = convert_to_list(char_count)
    char_count_list.sort(reverse=True, key=sort_on)

    for i in char_count_list:
        if i["char"].isalpha():
            print(f"The '{i['char']}' character was found {i['frequency']} times")

def get_file_contents(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def sort_on(dict):
    return dict["frequency"]

def main():
    file_path = "books/frankenstein.txt"

    file_contents = get_file_contents(file_path)
    word_count = get_count_words(file_contents)
    char_frequency = get_character_frequency(file_contents)
    
    print_report(file_path, word_count, char_frequency)

if __name__ == "__main__":
    main()