#Reads the entire contents of the book and returns it as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import word_counter
from stats import letter_counter

#orchestrator function
def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = word_counter(text)
    letter_count = letter_counter(text)
    print(f"{num_words} words found in the document")
    print(letter_count)
    
main()
    