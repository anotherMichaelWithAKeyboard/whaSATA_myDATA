import os # allows for functions to interact with the os environment.

from scipy.io.wavfile import write # writes audio to a wav file.

import threading # A Module that allows me to run tasks in series

import sounddevice as sd # allows to load audiofiles and write them back in different formats


folder_list = [r"whaSATA_myDATA", r"whaSATA_myDATA\Audio Files", r"whaSATA_myDATA\TextFiles"]
BASE_PATH = r"C:\Program Files"
AUDIO_FOLDER = os.path.join(BASE_PATH, "whaSATA_myDATA", "Audio Files")

# Creating the correct folders for multithreading TEST
def create_folders():
    for folder in folder_list:
        path = os.path.join(BASE_PATH, folder)
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            print("Folders already exist...")
            break


def record_audio(file_name, duration, fs=44100, channels=1, device=1):
    print("Recording audio...")

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels, device=device)
    sd.wait()
    print("Recording Finished")
    
    write(file_name, )





def main():
    create_folders()
    recording_time = 5 # Time to record audio clip
    audio_file = 'audio_clip.WAV' 

    t1 = threading.Thread(target= record_audio, args=(recording_time))

    t2 = 

if __name__ == "__main__":
    main()