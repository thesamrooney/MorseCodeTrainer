from multiprocessing.sharedctypes import Value
import numpy as np
from scipy.io import wavfile

#
# ITU Standard Morse Code generator
# 
# Please refer to the ITU standard for details (https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf)
#

class MorseGenerator:
    
    def __init__(self) -> None:
        self.sample_rate = 44100  # Hz
        self.standard_word = "PARIS"
        self.itu_char_set = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "É": "..-..",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "0": "-----",
            ".": ".-.-.-",
            ",": "--..--",
            ":": "---...",
            "?": "..--..",
            "'": ".----.",
            "-": "-....-",
            "/": "-..-.",
            "(": "-.--.",
            ")": "-.--.-",
            "\"": ".-..-.",
            "=": "-...-",
            "+": ".-.-.",
            "@": ".--.-.",
            " ": "/"
        }
        self.itu_special_chars = {
            "UNDERSTOOD": "...-.",
            "ERROR": "........",
            "INVITATION TO TRANSMIT": "-.-",
            "WAIT": ".-...",
            "END OF WORK": "...-.-",
            "START": "-.-.-"
        }

    def encode_morse(self, message:str) -> str:
        output = [""]
        for c in message:
            if c in self.itu_char_set.keys():
                if (c != " " and ("." or "-" in output[-1]) and output[-1] not in ["", "/"]):
                    output.append(" ")
                output.append(self.itu_char_set[c])
            else:
                raise ValueError("Character " + c + " not available in the ITU Morse Code spec. If this was a lowercase letter, try uppercasing your string before passing it to this method.")
        output.append("/")
        return "".join(output)

    def generate_timing(self, morse:str, farnsworth_timing:bool=True) -> str:
        output = [""]
        for c in morse:
            if c == ".":
                if ("-" in output[-1]):
                    output.append("_")
                output.append("-")
            elif c == "-":
                if ("-" in output[-1]):
                    output.append("_")
                output.append("---")
            elif c == " ":
                if farnsworth_timing:
                    output.append(" ")  # interchar spacing marker
                else:
                    output.append("___")  # ITU intercharacter timing: 3 low units
            elif c == "/":
                if farnsworth_timing:
                    output.append("/")  # interword spacing marker
                else:
                    output.append("_______")  # ITU interword timing: 7 low units
            else:
                raise ValueError("Invalid ITU Morse code character \"" + c + "\".")
        return "".join(output)

    def generate_audio(self, timing:str, fname:str="file.wav", freq:int=1000, wpm:int=20, farnsworth:int=-1, vol:int=100, smoothing_kernel:list=np.ones(100)/100) -> str:
        # we know a standard word is 50 units long (this is unit tested as well)
        unit_period = 1.2 / wpm  # in seconds. Formula taken from the ARRL Morse Transmission Timing Standard (see README.md)
        unit_len_i = len(np.arange(0, unit_period, 1/self.sample_rate))  # unit length as int

        low_unit = np.zeros((unit_len_i))
        high_unit = np.ones((unit_len_i))

        morse_heaviside = np.array([])

        if farnsworth <= 0 or farnsworth == wpm:
            # no Farnsworth compression
            # replace Farnsworth markers with unit lengths
            fixed_timing = timing.replace(" ", "___")  # inter-char spacing
            fixed_timing = fixed_timing.replace("/", "_______")  # inter-word spacing
            for c in fixed_timing:
                if c == "-":
                    morse_heaviside= np.append(morse_heaviside, high_unit)
                elif c == "_":
                    morse_heaviside= np.append(morse_heaviside, low_unit)
                else:
                    raise ValueError("Invalid timing character " + c + " in: " + timing)
        elif farnsworth < wpm:
            # valid Farnsworth compression
            # replace Farnsworth markers with their appropriate lengths of time
            # The following formulas are taken from the ARRL Morse Transmission Timing Standard (see README.md) where c = wpm and s = farnsworth

            t_a = ((60 * wpm) - (37.2 * farnsworth)) / (wpm * farnsworth)
            t_c = (3 / 19) * t_a  # inter-char spacing
            t_w = (7 / 19) * t_a  # inter-word spacing

            t_c_len_i = len(np.arange(0, t_c, 1/self.sample_rate))
            t_w_len_i = len(np.arange(0, t_w, 1/self.sample_rate))

            inter_char = np.zeros((t_c_len_i))
            inter_word = np.zeros((t_w_len_i))

            for c in timing:
                if c  == "-":
                    morse_heaviside = np.append(morse_heaviside, high_unit)
                elif c == "_":
                    morse_heaviside = np.append(morse_heaviside, low_unit)
                elif c == " ":
                    morse_heaviside = np.append(morse_heaviside, inter_char)
                elif c == "/":
                    morse_heaviside = np.append(morse_heaviside, inter_word)
                else:
                    raise ValueError("Invalid timing character " + c + " in: " + timing)
        
        for i in range(10):
            # add trailing silence; wavfile write function seems to cut off the last bit of audio
            morse_heaviside= np.append(morse_heaviside, low_unit)

        morse_heaviside = np.convolve(morse_heaviside, smoothing_kernel)

        signal_t = np.array(range(len(morse_heaviside))) * (1/self.sample_rate)
        signal = np.sin(2 * np.pi * freq * signal_t) * morse_heaviside * (vol / 100)
        int_signal = np.int16(signal * 32767)

        wavfile.write(fname, self.sample_rate, int_signal)






if __name__ == "__main__":
    gen = MorseGenerator()

    print("Testing that all alphanumeric characters work...")

    # Test text_to_morse function against all alphabetical characters
    assert gen.encode_morse("The quick brown fox jumped over the lazy dog".upper()) == "- .... ./--.- ..- .. -.-. -.-/-... .-. --- .-- -./..-. --- -..-/.--- ..- -- .--. . -../--- ...- . .-./- .... ./.-.. .- --.. -.--/-.. --- --./"

    # Test text_to_morse function against all numerical characters
    assert(gen.encode_morse("1234567890") == ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----/")


    print("Testing that many invalid characters cause exceptions...")

    for invalid_char in ",./!@#$%^&*()[]{}:;\"'\\|`~<>?-_=+\t\n\rabcdefghijklmnopqrstuvwxyz":
        # Note: lowercase chars not allowed
        try:
            gen.encode_morse(invalid_char)
            assert False, "Invalid character " + invalid_char + " should cause an exception!"
        except:
            assert True


    print("Testing timing string generator...")

    assert gen.generate_timing(".- .../---/", False) == "-_---___-_-_-_______---_---_---_______"

    # Check that all characters work:
    morsetext = gen.encode_morse("The quick brown fox jumps over the lazy dog".upper())

    try:
        gen.generate_timing(morsetext)
        assert True
    except ValueError:
        assert False, "morse_to_timing failed on the output of text_to_morse: " + morsetext 

    # check errors on most characters
    for invalid_char in ",!@#$%^&*()_[]{}:;\"'\\|`~<>?=+\t\n\rABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890":
        try:
            gen.generate_timing(invalid_char)
            assert False, "Invalid character " + invalid_char + " should cause an exception!"
        except ValueError:
            assert True

    print("Testing accented E.")

    # assert gen.encode_morse("é".upper()) == "..-../", "Accented E is a part of the ITU spec and should be accurately included."
    assert gen.encode_morse("É") == "..-../", "Accented E is a part of the ITU spec and should be accurately included."

    print("Testing number of time units in the standard word...")

    assert len(gen.generate_timing(gen.encode_morse(gen.standard_word), False)) == 50, "Standard word must have a timing length of 50 units."

    print("Testing successful!")