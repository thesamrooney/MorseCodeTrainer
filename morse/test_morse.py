from morse import text_to_morse


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



print("Testing successful!")
