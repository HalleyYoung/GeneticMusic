__author__ = 'halley'
from Note import *
import rhythmhelpers as rhy
import random
from music21 import *

def repitition(listOfLists):
    howManyBars = randint(0,3)
    # how many bars to be copied

    newList=[]

    s=set(range(1,5))
    # set of bars to which it can be copied: 1,2,3,4

    while p < howManyBars:
        fromBar = randint(0,4)
        toBar = random.choice(list(s)))
        s.remove(toBar)
        # remove that possible bar
        
# ADD MUTATIONS
        newList.insert(toBar,listOfLists[fromBar])
# ADD MUTATIONS
        p++
    return newList

def weightedRand():
    randNum = random.uniform(0,1)
    if randNum < .4:
        return 1
        # go up one
    elif .4 <= randNum < .7:
        return 0
        # repeat the note
    elif .7 <= randNum < .9:
        return 2
        # go up two
    elif .9 <= randNum < .95:
        return 3
        # go up three
    elif .95 <= randNum < 1:
        return 4

        # go up 4

#gen next chord note up or down a certain amount
def getNthChordNote(prev_note, cord, up_down = 1, how_many = 1):
    n = 0
    if prev_note > 14:
        up_down = -1
    while n < how_many:
        prev_note += up_down
        if prev_note % 7 in [i % 7 for i in cord]:
            n += 1
    return prev_note


#get a random chord note
def randomChordNote(prev_note, cord):
    upOrDown = 1 if random.uniform(0,1) < 0.6 else -1
    if prev_note >= 10:
        upOrDown = -1
    if prev_note >= 14:
        upOrDown = -1
        how_many = 2
    elif prev_note <= 4:
        upOrDown = 1
        how_many = 1
    else:
        how_many = 1 if random.uniform(0,1) < 0.9 else 2
    return getNthChordNote(prev_note, cord, upOrDown, how_many)

#generate chordal cells
def genChordal(rhythm, cord = [0,2,4], prev_note = 0):
    pitches = []
    for i in range(0, len(rhythm)):
        pitches.append(randomChordNote(prev_note, cord))
        prev_note = pitches[-1]
    return pitches

def genScalewise(rhythm, prev_note = None):
    # C=0, pitches = -12 to 12
    #rhythm: list of note, 1.0 = quarter notes, 2.0 = half, .5 = eigth -1 = rest
    if prev_note == None:
        prev_note = random.randint(-3,4)
    notes=[]
    notes.append(prev_note)

    for i in range(1, len(rhythm)):
        jump = weightedRand()
        upDown = random.randint(0,1)
        if upDown == 1:
            notes.append(notes[-1] + jump)
        elif upDown == 0:
            notes.append(notes[-1] - jump)
    return notes


def createInitial():
    chord = random.choice([[0,2,4],[4,6,8],[1,3,5]])
    notes = []
    prev_note = random.randint(-3,4)
    for i in range(0,3):
        for j in range(0,7):
            rhythm = rhy.randomDuration(2.0)
            if random.uniform(0,1) < 0.8:
                pits = genScalewise(rhythm, prev_note)
            else:
                pits = genChordal(rhythm, chord, prev_note)
            prev_note = pits[-1]
        notes.append([(pits[k],rhythm[k]) for k in range(0, len(rhythm))])
    return notes


initial = createInitial()
score = stream.Score()
for two_beats in initial:
    for pit, dur in two_beats:
        Note_object = Note(scale='0M', degree=pit, dur=dur)
        if Note_object.dur > 0:
            n = note.Note(pitToPitch(Pit(scale=Note_object.scale, degree=Note_object.degree + 35)))
            n.quarterLength = abs(Note_object.dur)
        else:
            n = note.Rest()
            n.quarterLength = abs(Note_object.dur)
        score.append(n)

score.show()
