
def print_first_last(words):
    first = words.pop(0)
    print ("first_word: ", first)
    print ("last word: ", words.pop(-1))

def break_words(sentence):
    words = sentence.split(' ')
    return words

def sort_words(words):
    words = sorted(words)
    return words

sentence = input ("Enter a sentence : ")
words = break_words(sentence)
print (words)

words = sort_words(words)
print (words)

print_first_last(words)
