__author__ = 'halley'
from Note import *
import rhythmhelpers as rhy
import random

def genScalewise(rhythm)

def createInitial():
    chord = random.choice([[0,2,4], [4,6,8], [1,3,5]])
    notes = []
    for i in range(0,3):
        for j in range(0,7):
            rhythm = rhy.randomDuration(2.0)
            if random.uniform(0,1) < 0.8:
                pits = genScalewise(rhythm)
            else:
                pits = genChordal(chord, rhythm)
