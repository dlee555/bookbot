from stats import *
import sys

def get_book_text(file):
    return file.read()


def main():
        
        if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            return sys.exit(1)

        with open(sys.argv[1]) as file:
            text = get_book_text(file)
            num_words = words_count(text)

            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {sys.argv[1]}...")
            print (f"----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")

            for key in char_count(text):
                 print(f"{key[0]}: {key[1]}")

            print("============= END ===============")

if __name__ == "__main__":
    main()