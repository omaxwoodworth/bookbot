import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

from stats import get_num_words, get_characters, get_sorted_list

def main():
    frank = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(frank)} total words")
    print("--------- Character Count -------")

    character_count = get_characters(frank)
    character_count = get_sorted_list(character_count)


    for pair in character_count:
        if pair["character"].isalpha():
            print(f"{pair["character"]}: {pair["count"]}")
    print("============= END ===============")

try:
    book_path = sys.argv[1]
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()