__author__ = 'halley'
from Note import *
import rhythmhelpers as rhy
import random


def weightedRand():
	randNum = random()
	if random < .4:
		return 1
		# go up one
	elif .4 <= random < .7:
		return 0
		# repeat the note
	elif .7 <= random < .9:
		return 2
		# go up two
	elif .9 <= random < .95:
		return 3
		# go up three
	elif .95 <= random < 1:
		return 4
		# go up 4

def genScalewise(rhythm):
	# C=0, pitches = -12 to 12
	#rhythm: list of note, 1.0 = quarter notes, 2.0 = half, .5 = eigth -1 = rest
	initialNote = randrange(-3,4)
	notes=[]
	notes[0]=initialNote
	l = 0

	while l < len(rhythm):
		jump = weightedRand()
		upDown = randrange(0,2)
		if upDown == 1:
			notes.append(notes[l] + jump)
		elif upDown == 0:
			notes.append(notes[l] - jump)
		l+=1
	return notes


def createInitial():
    chord = random.choice([[0,2,4], [4,6,8], [1,3,5]])
    notes = []
    for i in range(0,3):
        for j in range(0,7):
            rhythm = rhy.randomDuration(2.0)
            if random.uniform(0,1) < 0.8:
                pits = genScalewise(rhythm)
            	notes.append(pits)
            else:
                pits = genChordal(chord, rhythm)
                notes.append(pits)
    return notes
