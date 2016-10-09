#Aditya Vishwanath
import pyaudio
import wave
from note import get_note
from note import get_next_note
import numpy as np

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
TEMPO = 60 #beats per minute - modify this
SAMPLES_PER_SECOND = TEMPO / 60
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

one_note = []
#for i in range(0, int(RATE / (CHUNK * SAMPLES_PER_SECOND))):
#    data = stream.read(CHUNK)
#    print len(data)
#    for d in data:
#        one_note.append(d)
#print len(one_note)

while True:
    one_note = np.array([0])
    for i in range(0, int(RATE / (CHUNK * SAMPLES_PER_SECOND))):
        data = stream.read(CHUNK)
        # #print len(data)
        # for d in data:
        #     if d != None and len(d) != 0:
        #         one_note.append(d)
        temp_note = np.fromstring(data, dtype = np.int16)
        np.concatenate([one_note,temp_note])
    if len(one_note) != 0:
        print get_note(one_note)

    #print len(one_note)

    #one_note currently holds one second worth of data
    #Azra do magix with data and give Sarthak the mapped note

    #Sarthak do magix with the note and produce sound

#print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()


#wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#wf.setnchannels(CHANNELS)
#wf.setsampwidth(p.get_sample_size(FORMAT))
#wf.setframerate(RATE)
#wf.writeframes(b''.join(one_note))
#wf.close()
