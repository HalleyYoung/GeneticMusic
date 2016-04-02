__author__ = 'halley'
from Note import *

def fitness(notes, ties):
    rhythms = [i.dur for i in notes]
    degrees = [i.degree for i in notes]
    intervals = [degrees[i - 1] - degrees[i] for i in range(1, len(degrees))]
    fitness = 0
    fitness += hasChromaticRun(notes) * 50
    fitness += span(degrees)*50
    fitness += rhythmicDiversity(rhythms) * 50
    fitness += halfNotes(rhythms) * 50
    fitness += stepwise(intervals) * 50
    fitness += pitchDiversity(degrees) * 50
    fitness += bigJumps(intervals) * 50
    fitness += consecutiveJumps(intervals) * 50

def span(degrees):
    span = max(degrees) - min(degrees)
    if span < 5 or span > 10:
        return -1
    return 0


def hasChromaticRun(notes):
    has_run = False
    for i in range(1, len(notes) - 1):
        if notes[i - 1].degree == notes[i].degree and notes[i].sign == 1 or notes[i].sign == -1:
            has_run = True
            if notes[i].sign == 1:
                if not(notes[i + 1].degree == notes[i].degree + 1 and notes[i + 1].sign == 0):
                    return -1
            elif notes[i].sign == -1:
                 if not(notes[i + 1].degree == notes[i].degree - 1 and notes[i + 1].sign == 0):
                    return -1
    if has_run:
        return 1
    return 0


def rhythmicDiversity(rhythms):
    diversity = len(set(rhythms))
    if diversity < 3:
        return -1
    elif diversity > 5:
        return -1
    return 0

def halfNotes(rhythms):
    for i in range(1, len(rhythms)):
        if rhythms[i - 1] == 2.0 and rhythms[i] == 2.0:
            return -1
    if rhythms.count(2.0) > 4:
        return -1
    return 0


def stepwise(intervals):
    stepwise = filter(lambda i: abs(i) <= 1, intervals)
    if len(stepwise)/len(intervals) < 0.6:
        return -1
    return 0

def pitchDiversity(degrees):
    if len(set(degrees)) < 4:
        return -1
    elif len(set(degrees)) == 4:
        return -0.5
    return 0

def bigJumps(intervals):
    if max(map(abs, intervals)) > 4:
        return -1*(max(map(abs, intervals)) - 4)
    elif max(map(abs, intervals)) < 2:
        return -2
    return 0

def consecutiveJumps(intervals):
    minus = 0
    for i in range(1, len(intervals)):
        if abs(intervals[i - 1]) > 3 and abs(intervals[i]) > 3:
            minus -= 1
    return minus