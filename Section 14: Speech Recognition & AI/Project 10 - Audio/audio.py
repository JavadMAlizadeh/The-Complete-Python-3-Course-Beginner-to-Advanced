import pyaudio
import wave
import speech_recognition as sr
import subprocess
from Section_14.commands import Commander

running = True

def say(text):
    subprocess.call('ptts -u "k.txt"', shell=True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = sr.Recognizer()
cmd = Commander()

def initSpeech():
    print("Listening...")

    play_audio("./audio/audio_initiate.wav")

    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    play_audio("./audio/audio_end.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
        print(command)
        print("Thinking...")
    except:
        command = "Couldn't understand you"

    if command in cmd.exit:
        global running
        cmd.respond("Okay. Bye for now!")
        running = False

    elif command == "Couldn't understand you":
        cmd.respond("Couldn't understand you")
    else:
        cmd.discover(command)

while running == True:
    initSpeech()


