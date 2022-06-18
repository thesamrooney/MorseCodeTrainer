
import numpy as np
from scipy.io import wavfile

UNITS_PER_STANDARD_WORD = 50

class ToneGenerator():

    def __init__(self, wpm=20):
        self.sample_rate = 44100  # Hertz
        self.wpm = wpm
        self.time_unit_s = (60 / self.wpm) / UNITS_PER_STANDARD_WORD

    def create_tone(self, freq=1000, length=1.0, vol=1.0):
        # Frequency in Hz
        # Length in seconds
        # Volume in ratio
        t = np.arange(0, length, 1/self.sample_rate)
        tone = np.sin(2*np.pi*freq*t)*vol
        return tone

    def make_timing_function(self, timing: str):
        output = np.array([])

        num_pieces = len(np.arange(0, self.time_unit_s, 1/self.sample_rate))
        # print(str(num_pieces) + " pieces.")
        low_unit = np.zeros((num_pieces))
        # print("Finished low unit.")
        high_unit = np.ones((num_pieces))
        # print("Finished high unit.")

        for c in timing:
            if c == "-":
                # high: value of 1
                output = np.append(output, high_unit)
            elif c == "_":
                # low: value of 0
                output = np.append(output, low_unit)
            else:
                # invalid timing character
                raise ValueError("Invalid timing character " + c + " in: " + timing)

        return output

    def write_wav(self, name, signal):
        wavfile.write(name, self.sample_rate, signal)

    def write_morse_wav(self, timing, name="morse.wav", freq=1000, vol=1.0):
        # print("Starting...")
        morse_timing = self.make_timing_function(timing)
        # print("Created timing function: len = " + str(len(morse_timing)))
        tone = self.create_tone(freq=freq, length=len(morse_timing)/self.sample_rate, vol=vol)
        # print("Created tone: len = " + str(len(tone)))
        signal = np.int16(morse_timing * tone * 32767)
        # print("Created signal: len = " + str(len(signal)))
        self.write_wav(name, signal)
        # print("Wrote file.")

if __name__ == "__main__":
    gen = ToneGenerator(wpm=20)
    gen.write_morse_wav("-_-_-_---_---_---_-_-_-_______", name="sos.wav")
    