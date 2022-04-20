import sounddevice as sd
from pydub import AudioSegment
from pydub.silence import split_on_silence
import numpy as np
import soundfile as sf
from pathlib import Path
from tkinter import *
from tkinter.ttk import *
def rec(name,duration=10,fs=44100,channels=2):
    fs=44100
    duration = time  # seconds
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float32')
    print ("Recording Audio")
    sd.wait()
    print ("Audio recording complete , Play Audio")
    return myrecording,fs
def play(sound):
    sd.play(sound, fs)
    sd.wait()
    print ("Play Audio Complete")
def save(name,sound,fs):
    sf.write('./data/sound/'+name+'.wav',sound,fs)
def split(name,min_silence_len=500,silence_thresh=-40):
    sound = AudioSegment.from_wav('./data/sound/'+name+'.wav')
    # spliting audio files
    audio_chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-40 )
    #loop is used to iterate over the output list
    Path('./data/'+name).mkdir(parents=True,exist_ok=True)
    for i, chunk in enumerate(audio_chunks):
        output_file = "./data/"+name+"/{0}.wav".format(i)
        print("Exporting file", output_file)
        chunk.export(output_file, format="wav")
win=Tk()
win.title('Recoding')
brec=Button(master=win,text='Rec')
brec.bind(rec)
mainloop()