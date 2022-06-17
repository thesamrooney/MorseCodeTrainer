from morse import text_to_morse
from morse import morse_to_timing


print("Testing that all alphanumeric characters work...")

# Test text_to_morse function against all alphabetical characters
assert(text_to_morse("The quick brown fox jumped over the lazy dog") == "- .... ./--.- ..- .. -.-. -.-/-... .-. --- .-- -./..-. --- -..-/.--- ..- -- .--. . -../--- ...- . .-./- .... ./.-.. .- --.. -.--/-.. --- --./")

# Test text_to_morse function against all numerical characters
assert(text_to_morse("1234567890") == ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----/")


print("Testing that many invalid characters cause exceptions...")

for invalid_char in ",./!@#$%^&*()[]{}:;\"'\\|`~<>?-_=+\t\n\r":
    try:
        text_to_morse(invalid_char)
        assert False, "Invalid character " + invalid_char + " should cause an exception!"
    except:
        assert True


print("Testing timing string generator...")

assert morse_to_timing(".- .../---/") == "-_---___-_-_-_______---_---_---_______"

# Check that all characters work:
morsetext = text_to_morse("The quick brown fox jumps over the lazy dog")
try:
    morse_to_timing(morsetext)
    assert True
except ValueError:
    assert False, "morse_to_timing failed on the output of text_to_morse: " + morsetext 

# check errors on most characters
for invalid_char in ",!@#$%^&*()_[]{}:;\"'\\|`~<>?=+\t\n\rABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890":
    try:
        morse_to_timing(invalid_char)
        assert False, "Invalid character " + invalid_char + " should cause an exception!"
    except ValueError:
        assert True


print("Testing successful!")
