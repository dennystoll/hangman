fh = open("/home/dennstoll/code/games/hangman/words.txt" , "rt")

word_list = []

def words_list():
    for words in fh:
        line = words.rstrip()
        word = line.split()
        word_list.append(word)
    return word_list