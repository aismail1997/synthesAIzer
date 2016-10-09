import random
import time

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
while(1):
    fb = open("potato.txt", 'w')
    note = random.choice(notes)
    print(note)
    fb.write(note + "\n")
    time.sleep(1)
