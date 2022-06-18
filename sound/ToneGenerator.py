
import numpy as np
from scipy.io import wavfile

class ToneGenerator():

    def __init__(self):
        self.sample_rate = 44100  # Hertz

    def create_tone(self, freq=1000, length=1.0, vol=1.0):
        # Frequency in Hz
        # Length in seconds
        # Volume in ratio
        t = np.arange(0, length, 1/self.sample_rate)
        tone = np.int16(np.sin(2*np.pi*freq*t)*32767*vol)

    def make_timing_function(self, timing: str):
        output = np.array()
        for c in timing:
            if c == "-":
                # high: value of 1
                for i in np.arange(0, self.time_unit_s, 1/self.sample_rate):
                    np.append(output, [1])
            elif c == "_":
                # low: value of 0
                for i in np.arange(0, self.time_unit_s, 1/self.sample_rate):
                    np.append(output, [0])
            else:
                # invalid timing character
                raise ValueError("Invalid timing character " + c + " in: " + timing)
        return output

    def write_wav(self, name, signal):
        wavfile.write(name, self.sample_rate, signal)


