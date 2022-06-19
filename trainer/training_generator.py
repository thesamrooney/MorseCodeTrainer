
from numpy import array
from trainer.word_filter import WordFilter
import random

class TrainingDataGenerator:
    
    def __init__(self) -> None:
        self.words = []
        mit_10k = open("./trainer/resources/mit_10k_words.txt", "r")
        for word in mit_10k:
            self.words.append(word.strip())
        mit_10k.close()

    def random_chars(self, selection:list, num_groups:int=5, group_size:int=5):
        output = []
        for i in range(num_groups):
            for j in range(group_size):
                output.append(random.choice(selection))
            output.append(" ")
        return "".join(output)

    def random_english(self, num_words:int=5, available_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@()-+=/.,:'\"? "):
        filt = WordFilter(available_chars)
        selected_words = random.sample(list(filter(filt.check_word, self.words)), num_words)
        return " ".join(selected_words).replace("\n", "")
