import sys
from stats import count_characters, sort_characters

def word_count(content):
    return len(content.split())

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    try:
        with open(book_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found.")
        sys.exit(1)

    print("----------- Word Count ----------")
    print(f"Found {word_count(content)} total words")

    print("--------- Character Count -------")
    char_counts = count_characters(content)
    sorted_chars = sort_characters(char_counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
