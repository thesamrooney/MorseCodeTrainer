

# The standard word used for words-per-minute calculation.
from multiprocessing.sharedctypes import Value


STANDARD_WORD = "PARIS "

# International Morse Code characters
ITU_CHARS = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "0": "----- ",
    " ": "/"
}


"""
Encode an alphanumeric string in Morse code using the ITU (International Morse Code) alphabet.
"""
def encode_text(text: str):
    # ignore case, remove leading and trailing spaces
    up_text = text.upper().strip()  
    output = ""

    for c in up_text:
        if c in ITU_CHARS.keys():
            if c == " " and len(output) > 0:
                # remove trailing spaces when we end a word
                output = output.strip()
            output += ITU_CHARS[c]
        else:
            raise ValueError("Parameter string contained illegal character " + c + ": " + text)

    if len(output) != 0 and output[-1] != "/":
        output = output.strip() + "/"

    return output


"""
Convert Morse Code string into timing string.
The output will only contain dashes and underscores, indicating on and off respectively.

Rules:
- A dit (.) is equal to one unit of time.
- A dah (-) is equal to three units of time.
- Two elements of the same character are separated by one off unit of time.

Rules below may be warped by Farnsworth compression.

- Two characters are separated by three off units of time.
- Two words are separated by seven off units of time.
"""
def get_timing(morse: str):
    
    output = ""
    for c in morse:
        if c == ".":
            output += "-_"  # one space between every character
        elif c == "-":
            output += "---_"  # one space between every character
        elif c == " ":
            output += "__"  # extend space to three units
        elif c == "/":
            output += "______"  # extend space to seven units
        else:
            raise ValueError("Invalid character " + c + " included in Morse Code input: " + morse)
    
    return output



if __name__ == "__main__":
    print(encode_text("The quick brown fox jumped over the lazy dog"))
    print(get_timing(encode_text(STANDARD_WORD)))
