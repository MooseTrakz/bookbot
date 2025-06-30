
from stats import get_num_words, get_num_char_sym

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print ("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")
    print (get_num_char_sym(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
