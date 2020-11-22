import time ,sys
import argparse
from CommandRecorder import recordCommandPyAudio, recordCommandSounddevice
from CommandRecognizer import Recognizer
# from GameInterface import GameInterface
from KeyLogging import pressKeyMario,pressKeyTetris
# yes, no, up, down, left, right, on, off, stop, go

if __name__ == "__main__":

    window_len = 500
    recording_len = 1.5
    recognizer = Recognizer()
    parser = argparse.ArgumentParser()
    parser.add_argument("game", help="add name of the game (mario/tetris)")
    args = parser.parse_args()
    if(args.game!="mario" and args.game!="tetris"):
        print("Add tetris or mario as arguments")
        sys.exit()
    # gameInterface = GameInterface()
    while True:

        start_time = time.time()
        command = recordCommandSounddevice(duration=recording_len, playback=False) # 1500
        command = recognizer.classifyCommand(command,window_len,recording_len)
        end_time = time.time()
        command_input_delay = (end_time - start_time)
        print('Command input delay: {:0.4f}s'.format(command_input_delay))
        # gameInterface.processCommand(command)
        if(args.game=="mario"):
            pressKeyMario(command)
        elif(args.game=="tetris"):
            pressKeyTetris(command)