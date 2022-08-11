## TODO
- [x] Morse audio
    - [x] Generate Morse code messages from text
        - [x] Generate ITU-standard Morse code
    - [x] Generate timing strings from Morse code
    - [x] Generate sound from timing strings
        - [x] Include settings for WPM, frequency, and volume
        - [x] Save sounds to file (.wav)
    - [x] Implement Farnsworth timing
    - [x] Play pre-generated sound (playsound library)
    - [ ] Switch to [python-sounddevice](https://python-sounddevice.readthedocs.io/en/0.3.10/) library?

- [x] Code structure
    - [x] Single class for text conversion/audio generation workflow

- [ ] Trainer
    - [x] Generate training data
        - [x] Random character mode (with limited selection of characters)
        - [x] Random English words mode (with limited selection of characters)
            - [x] Filter word list (clean words only!) (done manually, likely better to find a new word list)
        - [ ] Excerpts from the wild? (for review mode)
    - [ ] Session
        - [ ] Investigate session length(s)
        - [ ] Multiple types of sessions?
            - [ ] Character introduction
            - [ ] Review session
            - [ ] Knowledge maintenance session
        - [ ] Grading
            - [ ] Automatically calculated accuracy %
            - [ ] Grade by word, then by letter?
    - [ ] Progression
        - [x] Character learn order
        - [ ] Save progress per character
        - [ ] Save progress in CSV format (for later graphing)?
    - [ ] GUI
        - [x] Investigate cross-platform GUI libraries (Qt5)
            - [ ] Would a mobile app be worth it?
        - [x] Implement "listen to new chars" button
        - [x] Implement "listed to level" button
        - [ ] Implement "auto grade" button
        - [ ] Graphing progress?
        - [ ] Create flow chart / state machine for GUI flow
