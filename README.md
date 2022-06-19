# Morse Code Trainer Project

Goal: Teach the user to recognize Morse code messages by generating and playing audio/visual Morse code messages.

## Koch method

Named after psychologist Ludwig Koch, this method involves sending characters at the learner's target speed, but only sending a limited number of characters at a time. 

Begin by sending a long string which only contains two unique characters.
Then, get input from the learner of what they thought the message was.
Compare that with reality and calculate a percentage score: if the learner scores above 90%, continue. If not, try again.

When the user is 90% accurate add another unique character and repeat until the learner is again at 90% accuracy.
Repeat this process until all characters are in play.

## Farnsworth timing

Farnsworth timing, invented by Donald R. Farnsworth (W6TTB) in the 1950s, is a method of slowing down the rate at which words are sent in Morse code without slowing down the speed of the charaters themselves. 

Typically, the time between character elements is kept at 20-35 words per minute, while the time between characters and words may be slowed down to as low as 5 words per minute. A more in-depth explanation is available on the ARRL website, link below.

## Resources

An excellent resource on the Koch method is available on [qsl.net](https://www.qsl.net/n1irz/finley.morse.html).

The ARRL standard for Farnsworth timing is on [arrl.org](http://www.arrl.org/files/file/Technology/x9004008.pdf). 
Please note that this document includes the ARRL Morse Transmission Timing Standard used in this program.

The ITU Morse Code standard is located on [itu.int](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf).

For the English words mode, we use a [list of 10k words](https://www.mit.edu/~ecprice/wordlist.10000) from MIT. PLEASE NOTE! This list is *not* yet filtered for kid-friendly words.

## TODO
- [x] Morse audio
    - [x] Generate Morse code messages from text
        - [x] Generate ITU-standard Morse code
    - [x] Generate timing strings from Morse code
    - [x] Generate sound from timing strings
        - [x] Include settings for WPM, frequency, and volume
        - [x] Save sounds to file
    - [x] Implement Farnsworth timing
    - [x] Play pre-generated sound (playsound library)

- [x] Code structure
    - [x] Single class for full audio/text generation workflow

- [ ] Trainer
    - [x] Generate training audio
        - [x] Random character mode (with limited selection of characters)
        - [x] Random English words mode (with limited selection of characters)
            - [ ] Filter word list (clean words only!)
        - [ ] Excerpts from the wild? (for review mode)
    - [ ] Session
        - [ ] Investigate session length(s)
        - [ ] Progression
            - [ ] Overall accuracy above 90%?
            - [ ] Specific characters or random?
        - [ ] Multiple types of sessions?
            - [ ] Character introduction
            - [ ] Review session
            - [ ] Knowledge maintenance session
    - [ ] Grading
        - [ ] Grade individual words
        - [ ] Change grading based on session length?
    - [ ] Save progress
        - [ ] Save accuracy by character
        - [ ] Save character progress
        - [ ] Save datetime of session?
        - [ ] Graph progress
            - [ ] Matplotlib, or another library?
            - [ ] By datetime?
            - [ ] By session?
        - [ ] Save data as CSV
    - [ ] GUI
        - [ ] Investigate cross-platform GUI libraries
            - [ ] Would a mobile app be worth it?
        - [ ] Create flow chart / state machine for GUI flow

