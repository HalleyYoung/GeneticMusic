__author__ = 'halley'
import fitness
import functionalhelpers as fh
from music21 import *
from Note import *


candidates = []

for i in range(0,400):
    fitnesses_and_candidates = zip(map(fitness.fitness, candidates), candidates)
    fitnesses_and_candidates.sort(reverse=True, key=lambda i:i[0])
    bests = [i[1] for i in fitnesses_and_candidates[:50]]
    candidates = fh.concat(map(genVariations, bests))


best_score = stream.Score()
for note_ in bests[0]:
    n = note.Note(pitToPitch(note_.pit))
    n.quarterLength = note_.dur
    best_score.append(n)

best_score.show()

