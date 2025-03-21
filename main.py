#Reads the entire contents of the book and returns it as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

#Accepts text from book as a string and returns the number of words
def word_counter(text):
    count = 0
    word_list = text.split()
    for word in word_list:
        count += 1
    return count


#orchestrator function
def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = word_counter(text)
    print(f"{num_words} words found in the document")
    
main()
    