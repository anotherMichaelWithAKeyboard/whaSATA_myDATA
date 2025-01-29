import os # allows for functions to interact with the os environment.

import shutil # more powerful os module (used for copying files)

from scipy.io.wavfile import write # writes audio to a wav file.

import threading # A Module that allows me to run tasks in series

import sounddevice as sd # allows to load audiofiles and write them back in different formats

import time 

import whisper # whisper AI transcription Module

# Folder Paths
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

# Function that records for duration(seconds) and saves audiofile on local disc in location BASE_PATH
def record_audio(audio_file='audio_clip.WAV', duration=15, fs=44100, channels=1, device=1):
    print("Recording audio...")

    # Begins recording
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels, device=device)
    sd.wait() # waits until the recording is finished
    print("Recording Finished")
    
    # Saves Recording
    write(audio_file, fs, recording)
    print("Saved temp Recording")

    # Move audio recording to temp storage
    shutil.move(audio_file, AUDIO_FOLDER)
    print(f"Moved {audio_file} to {AUDIO_FOLDER}")
    
    os.remove(os.path.join(AUDIO_FOLDER, audio_file)) # Removes temp save
    print("Deleted file")

def transcribe_audio(audio_file='audio_clip.WAV'):
    file_path = os.path.join(AUDIO_FOLDER, audio_file)

    model = whisper.load_model('small', device='cuda')
    print("Transcribing audio...")

    result = model.transcribe(file_path, language='en', verbose=True)

    transcription = result['text']
    segments = result['segments'] # takes list of segments out of result
    print("Transcription Completed.")
    print("\nTranscription with timestamps:")
    for segment in segments:
        start_time = segment['start']   # pull start_time from each segment
        end_time = segment['end']       # pull end_time from each segment
        text = segment['text']          # pull text from each segment.
        print(f"[{start_time:.2f} - {end_time:.2f}] {text}")

    # edit note- pull variables for realigning.

#-------------------------------------------------------------------------
#------------------------Test Functions---------------------------------
# Simple counting function to Test multithreading
def stall_temp_task_test():
    count = 0
    for i in range(15):
        count+=1
        print(count)
        time.sleep(1)

#------------------------------------------------------------------------
#------------------------------------------------------------------------
# Recursive loop that runs all the tasks in parallel 
def transcription_loop():
    
    # initialise the functions on a thread.
    # t1 = threading.Thread(target= record_audio)
    t2 = threading.Thread(target=stall_temp_task_test)
    t3 = threading.Thread(target= transcribe_audio)
    #t4 =  threading.Thread(target= )

    # Run functions
    #t1.start()
    #t2.start()
    t3.start()
    t2.start()
    #t4.start()


def main():
    #create_folders()
    transcription_loop()
    #transcribe_audio()



if __name__ == "__main__":
    main()