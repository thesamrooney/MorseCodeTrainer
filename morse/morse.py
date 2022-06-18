

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

    print("Testing that all alphanumeric characters work...")

    # Test text_to_morse function against all alphabetical characters
    assert(encode_text("The quick brown fox jumped over the lazy dog") == "- .... ./--.- ..- .. -.-. -.-/-... .-. --- .-- -./..-. --- -..-/.--- ..- -- .--. . -../--- ...- . .-./- .... ./.-.. .- --.. -.--/-.. --- --./")

    # Test text_to_morse function against all numerical characters
    assert(encode_text("1234567890") == ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----/")


    print("Testing that many invalid characters cause exceptions...")

    for invalid_char in ",./!@#$%^&*()[]{}:;\"'\\|`~<>?-_=+\t\n\r":
        try:
            encode_text(invalid_char)
            assert False, "Invalid character " + invalid_char + " should cause an exception!"
        except:
            assert True


    print("Testing timing string generator...")

    assert get_timing(".- .../---/") == "-_---___-_-_-_______---_---_---_______"

    # Check that all characters work:
    morsetext = encode_text("The quick brown fox jumps over the lazy dog")
    try:
        get_timing(morsetext)
        assert True
    except ValueError:
        assert False, "morse_to_timing failed on the output of text_to_morse: " + morsetext 

    # check errors on most characters
    for invalid_char in ",!@#$%^&*()_[]{}:;\"'\\|`~<>?=+\t\n\rABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890":
        try:
            get_timing(invalid_char)
            assert False, "Invalid character " + invalid_char + " should cause an exception!"
        except ValueError:
            assert True

    print("Testing number of time units in the standard word...")

    assert len(get_timing(encode_text(STANDARD_WORD))) == 50, "Standard word must have a timing length of 50 units."

    print("Testing successful!")
