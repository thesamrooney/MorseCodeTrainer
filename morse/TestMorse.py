from Morse import encode_text
from Morse import get_timing
from Morse import STANDARD_WORD


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
