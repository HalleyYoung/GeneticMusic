__author__ = 'halley'
from music21 import *
from Note import pitToPitch

def notesToScore(notes):
    score = stream.Score()
    for note_ in notes:
        n = note.Note(pitToPitch(note_.pit))
        n.quarterLength = note_.dur
        score.append(n)

    score.show()
    return score