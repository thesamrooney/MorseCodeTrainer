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

For the English words mode, we use a [list of 10k words](https://www.mit.edu/~ecprice/wordlist.10000) from MIT. PLEASE NOTE! This list may still contain non-kid-friendly words. Currently looking out for a properly filtered list.

This program uses the same word order as [lcwo.net](https://lcwo.net), the popular online Morse code training tool.

## Dependencies

numpy (to generate audio)

scipy (to create .wav files from numpy audio)

playsound v1.2.2 (to play .wav files)

pyqt5 (for GUI)
