import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit (1)

path_to_file = sys.argv[1]

#Reads the entire contents of the book and returns it as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import word_counter
from stats import letter_counter
from stats import list_creator

#orchestrator function
def main():
    text = get_book_text(path_to_file)
    num_words = word_counter(text)
    letter_count = letter_counter(text)
    sorted_list = list_creator(letter_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for i in sorted_list:
        print (f"{i["char"]}: {i["count"]}")
    
    print("============= END ===============")
    
main()
    