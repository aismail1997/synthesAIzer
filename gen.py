import random
import time

# notes = ["A", "B", "C", "D", "E", "F", "G"]
notes = ["C", "D", "E", "G", "A"]
while(1):
    fb = open("potato.txt", 'w')
    note = random.choice(notes)
    print(note)
    fb.write(note + "\n")
    time.sleep(1)
