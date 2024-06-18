def main():
    file_contents = ""
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"{count_words(file_contents)} words found in the file")

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

main()
