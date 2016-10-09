import numpy.fft as fft

# map of frequencies to notes
def get_note(data):
    notes_map = {'C': 261.63 ,'C#': 277.18,'D': 293.66, 'D#': 311.13, 'E': 329.63, 'F': 349.23, 'F#': 369.99, 'G': 392, 'G#': 415.3, 'A': 440, 'A#': 466.16,'B': 493.88}
    spectrum = fft.fft(data) # doing an fft on the data to get frequency spectrum
    freq = fft.fftfreq(len(spectrum)) # get the frequencies
    currentfreq = max(abs(spectrum))
    print str(len(spectrum)) + ' ' + str(currentfreq)
    currentnote = 'C'
    for note in notes_map:
        if (abs(currentfreq - notes_map[note]) < 15):
            currentnote = note
            break;
    return currentnote

# 1-1 mapping

def get_next_note(currentnote):
    nextnotes_map = {'C': 'E' ,'C#': 'F', 'D': 'F', 'D#': 'G', 'E': 'G', 'F': 'A' , 'F#': 'A', 'G': 'E', 'G#': 'A#', 'A': 'F', 'A#': 'A', 'B': 'G'}
    nextnote = nextnotes_map[currentnote]
    return nextnote
