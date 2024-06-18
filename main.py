def main():
    file = "./books/frankenstein.txt"
    file_contents = ""
    with open(file) as f:
        file_contents = f.read()
    print(f"--- Begin report of {file} ---")
    print(f"{count_words(file_contents)} words found in the file\n")
    chars = count_characters(file_contents)

    chars = dict(sorted(chars.items(), key=lambda x:x[1], reverse=True))
    for key in chars:
        if key.isalpha():
            print(f"The '{key}' character was found {chars[key]} times")
    print("--- End report ---")

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    characters = {}
    for char in file_contents:
        if char.lower() not in characters:
            characters[char.lower()] = 1
        else:
            characters[char.lower()] += 1
    return characters

main()
