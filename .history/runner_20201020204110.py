import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

def if __name__ == "__main__": 
    while True:
        rate = 44100
        command = recordCommandSounddevice()        
        sd.play(command, rate)