#Accepts text from book as a string and returns the number of words
def word_counter(text):
    count = 0
    word_list = text.split()
    for word in word_list:
        count += 1
    return count