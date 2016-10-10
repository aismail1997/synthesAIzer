import numpy.fft as fft
import numpy as np
import operator

# map of frequencies to notes
def get_note(data):
    notes_map = {'C': 785 , 'C1': 1309, 'C2': 2096,'C#': 547,'D': 583, 'D#': 307, 'E': 328, 'F': 1381, 'F#': 748, 'G': 1185, 'G1': 2359,'G#': 1218, 'A': 438, 'A#': 2751,'B': 984}
    # applying fft to data stream from microphone
    fourier = fft.fft(data)
    frequencies = fft.fftfreq(len(data))  # assuming no delay, get all frequencies in the fft
    positive_frequencies = frequencies[np.where(frequencies > 0)]
    magnitudes = abs(fourier[np.where(frequencies > 0)]) # magnitude spectrum
    peak_frequency = np.argmax(magnitudes) # determine most prominent frequency
    # defaultnotes = ['C', 'E', 'G', 'B'] # default frequency
    # currentnote = defaultnotes[peak_frequency % 4]
    currentnote = "\n"
    #print str(= peak_frequency)
    # map frequency to note with a certain range of error
    for note in notes_map:
        if (abs(peak_frequency - notes_map[note]) < 15):
            currentnote = note
            break;
    return currentnote

# 1-1 mapping

def get_next_note(currentnote):
    nextnotes_map = {'C': 'E', 'C1': 'E', 'C2': 'E', 'C#': 'F', 'D': 'F', 'D#': 'G', 'E': 'G', 'F': 'A' , 'F#': 'A', 'G': 'E', 'G1': 'E', 'G#': 'A#', 'A': 'F', 'A#': 'A', 'B': 'G'}
    nextnote = nextnotes_map[currentnote]
    return nextnote
