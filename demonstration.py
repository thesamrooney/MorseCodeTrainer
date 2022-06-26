
from playsound import playsound # NOTE: use playsound version 1.2.2
from morse.morse_generator import MorseGenerator
from trainer.training_generator import TrainingDataGenerator

name = "morse.wav"
gen = MorseGenerator()
datagen = TrainingDataGenerator()

morse_words = datagen.random_english(3)

gen.generate_audio(gen.generate_timing(gen.encode_morse(morse_words), farnsworth_timing=True), farnsworth=15, wpm=35)

playsound("file.wav")

print(morse_words)


