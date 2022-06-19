
from numpy import array
import random

class TrainingDataGenerator:
    
    def __init__(self) -> None:
        self.words = []
        mit_10k = open("./trainer/resources/mit_10k_words.txt", "r")
        for word in mit_10k:
            self.words.append(word.strip())
        mit_10k.close()

    def random_chars(self, selection:list="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@()-+=/.,:'\"? ", num_groups:int=5, group_size:int=5):
        output = []
        for i in range(num_groups):
            for j in range(group_size):
                output.append(random.choice(selection))
            output.append(" ")
        return "".join(output)

    def random_english(self, num_words:int=5, available_chars:list="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@()-+=/.,:'\"? "):
        filt = WordFilter(available_chars)
        selected_words = random.sample(list(filter(filt.check_word, self.words)), num_words)
        return " ".join(selected_words).replace("\n", "")


class WordFilter:

    def __init__(self, available_chars:list):
        self.char_selection = available_chars

    def check_word(self, word:str):
        for c in word:
            if c not in self.char_selection:
                return False
        return True


if __name__ == "__main__":
    # for TrainingDataGenerator
    gen = TrainingDataGenerator()
    print(gen.random_chars())
    print(gen.random_english())


    # for WordFilter
    words = []
    mit_10k = open("./trainer/resources/mit_10k_words.txt", "r")
    for word in mit_10k:
        words.append(word.strip())
    mit_10k.close()

    filt = WordFilter("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@()-+=/.,:'\"? ")

    print(random.sample(list(filter(filt.check_word, words)), 5))