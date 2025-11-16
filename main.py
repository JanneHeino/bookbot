from stats import words_in_book, count_characters, sort_dict
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()





def main():
    # book = get_book_text("books/frankenstein.txt")
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    print(f"Found {words_in_book(book)} total words")
    book_characters = count_characters(book)
    # print(book_characters)
    sorted_chars = sort_dict(book_characters)

    for a in sorted_chars:
        if a["char"].isalpha():
            print(f"{a["char"]}: {a["num"]}")

main()