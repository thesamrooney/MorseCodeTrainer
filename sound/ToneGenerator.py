
import numpy as np
from scipy.io import wavfile

class ToneGenerator():

    def __init__(self):
        self.sample_rate = 44100  # Hertz

    def createTone(self, freq=1000, length=1.0, vol=1.0):
        # Frequency in Hz
        # Length in seconds
        # Volume in ratio
        t = np.arange(0, length, 1/self.sample_rate)
        tone = np.int16(np.sin(2*np.pi*freq*t)*32767*vol)

    def writeWav(self, name, signal):
        wavfile.write(name, self.sample_rate, signal)


