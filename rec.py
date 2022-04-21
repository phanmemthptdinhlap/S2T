import sounddevice as sd
from pydub import AudioSegment
from pydub.silence import split_on_silence
import numpy as np
import soundfile as sf
from pathlib import Path
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
def rec_audio(duration=10,fs=44100,channels=2):
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float32')
    print ("Recording Audio")
    sd.wait()
    print ("Audio recording complete , Play Audio")
    return myrecording,fs
def play_audio(sound,fs):
    sd.play(sound, fs)
    sd.wait()
    print ("Play Audio Complete")
def save_audio(name,sound,fs):
    sf.write('./data/sound/'+name+'.wav',sound,fs)
def split_audio(name,min_silence_len=500,silence_thresh=-40):
    sound = AudioSegment.from_wav('./data/sound/'+name+'.wav')
    # spliting audio files
    audio_chunks = split_on_silence(sound, min_silence_len=100, silence_thresh=-30 )
    #loop is used to iterate over the output list
    Path('./data/'+name).mkdir(parents=True,exist_ok=True)
    for i, chunk in enumerate(audio_chunks):
        output_file = "./data/"+name+"/{0}.wav".format(i)
        print("Exporting file", output_file)
        chunk.export(output_file, format="wav")

class RecApp(App):

    def build(self):
        def save(nstance):
            def save_split(instance):
                msbox.dismiss()
                split_audio(text.text)
            mspanel=BoxLayout(orientation='vertical')
            mstext=TextInput(hint_text='index',multiline=False)
            msbut=Button(text='Save && Split')
            msbut.bind(on_press=save_split)
            mspanel.add_widget(mstext)
            mspanel.add_widget(msbut)
            msbox = Popup(title='Save && Split',content=mspanel,size_hint=(None, None), size=(400, 400))
            msbox.open()
        def rec(instance):
            myrec,fs=rec_audio()
            play_audio(myrec,fs)
            save_audio(text.text,myrec,fs)
        panel=BoxLayout(orientation='vertical')
        butrec=Button(text='Rec')
        butrec.bind(on_press=rec)
        butsave=Button(text='Save')
        butsave.bind(on_press=save)
        text=TextInput(hint_text='name',multiline=False)
        panel.add_widget(text)
        panel.add_widget(butrec)
        panel.add_widget(butsave)
        return panel
RecApp().run()