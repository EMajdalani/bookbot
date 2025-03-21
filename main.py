#Reads the entire contents of the book and returns it as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

#orchestrator function
def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    print(text)
    
main()
    