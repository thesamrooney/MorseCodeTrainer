
from pyparsing import Word


class WordFilter:

    def __init__(self, available_chars:list):
        self.char_selection = available_chars

    def check_word(self, word:str):
        for c in word:
            if c not in self.char_selection:
                return False
        return True


if __name__ == "__main__":
    import random

    words = []
    mit_10k = open("./trainer/resources/mit_10k_words.txt", "r")
    for word in mit_10k:
        words.append(word.strip())
    mit_10k.close()

    filt = WordFilter("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@()-+=/.,:'\"? ")

    print(random.sample(list(filter(filt.check_word, words)), 5))
