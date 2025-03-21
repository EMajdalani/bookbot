#Accepts text from book as a string and returns the number of words
def word_counter(text):
    count = 0
    word_list = text.split()
    for word in word_list:
        count += 1
    return count

#takes the text from the book and returns the number of times each character appears
def letter_counter(text):
    lowercase = text.lower()
    letter_count = {}
    for character in lowercase:
        if character in letter_count:
            letter_count[character] += 1
        else:
            letter_count[character] = 1
    return letter_count
    

#takes the dictionary and returns a sorted list of letters
def list_creator(letter_count):
    letter_list = []
    for letter in letter_count:
        if letter.isalpha() == True:
            letter_list.append({"char": letter, "count": letter_count[letter]})

    #sorter
    def sort_by(dict_item):
        return dict_item["count"]
    
    letter_list.sort(reverse=True, key=sort_by)

    return letter_list


