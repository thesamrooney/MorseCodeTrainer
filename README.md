# Morse Code Trainer Project

Goal: Teach the user to recognize Morse code messages by generating and playing audio/visual Morse code messages.

## Koch method

Named after psychologist Ludwig Koch, this method involves sending characters at the learner's target speed, but only sending a limited number of characters at a time. 

Begin by sending a long string which only contains two unique characters.
Then, get input from the learner of what they thought the message was.
Compare that with reality and calculate a percentage score: if the learner scores above 90%, continue. If not, try again.

When the user is 90% accurate add another unique character and repeat until the learner is again at 90% accuracy.
Repeat this process until all characters are in play.

An excellent resource on the Koch method is available on [qsl.net](https://www.qsl.net/n1irz/finley.morse.html).

## TODO
- [x] Generate Morse code messages from text
- [x] Generate timing strings from Morse code
- [ ] Generate sound from timing strings
    - [ ] Include settings for WPM, frequency, and volume
    - [ ] Investigate Farnsworth timing?
- [ ] Play pre-generated sound
- [ ] Create GUI


