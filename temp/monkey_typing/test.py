import re

def count_words(text, words):
    total = 0
    for item in words:
        print item
        if re.search(item, text) != 0:
            total = total + 1
            print total

if __name__ == "__main__":
    text = ('How aresjfldfadfadf you?')
    words = {'you', 'how', 'hello', 'are'}
    count_words(text, words)



