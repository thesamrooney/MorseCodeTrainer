

# The standard word used for words-per-minute calculation.
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


def text_to_morse(text: str):
    # convert a string of characters to a Morse Code string.

    up_text = text.upper()  # ignore case
    output = ""

    for c in up_text:
        if c in ITU_CHARS.keys():
            if c == " " and len(output) > 0:
                output = output.strip()  # remove trailing spaces when we end a word
            output += ITU_CHARS[c]
        else:
            raise ValueError("Parameter string contained illegal character " + c + ": " + text)

    if len(output) != 0 and output[-1] != "/":
        output = output.strip() + "/"

    return output




if __name__ == "__main__":
    print(text_to_morse("The quick brown fox jumped over the lazy dog"))
    print(text_to_morse(STANDARD_WORD))
