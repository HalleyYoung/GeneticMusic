__author__ = 'halley'

scale_names = ["C", "Cs", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
degree_names = {'M': ["I", "ii", "iii", "IV", "V", "vi", "vii"],
                'm': ["i", "ii", "III", 'iv', 'v', 'VI', 'VII']}

class Pit():
    def __init__(self, midi=None, scale=None, degree=None, sign=0):
        self.midi = midi
        self.scale = scale
        self.degree = degree
        self.sign = sign
        if self.midi is None and self.scale is not None and self.degree is not None:
            scale = scales[self.scale]
            sign = 0 if self.sign is None else self.sign
            self.midi = scale[degree % len(scale)].midi + (degree/len(scale)) * 12 + sign

white_keys = [0, 2, 4, 5, 7, 9, 11]
next = {0: [0, 1, 2, 3, 4, 5, 6],
        1: [3, 4, 0],
        2: [3],
        3: [0, 4],
        4: [0, 3, 5],
        5: [1, 4],
        6: [0]}

prev = dict([(i, []) for i in range(0, 7)])
for k, values in next.items():
    for value in values:
        prev[value].append(k)
scales = {}

signs = {}
signs['M'] = [0, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1]
signs['m'] = []
for i in range(0, 12):
    signs['m'].append(signs['M'][(i + 3) % 12])

scales['major'] = [0, 2, 4, 5, 7, 9, 11]
scales['minor'] = [0, 2, 3, 5, 7, 8, 10]
for i in range(0, 12):
    scales[i] = [Pit(midi=j + i) for j in scales['major']]
    for k in range(0, len(scales[i])):
        if scales[i][k].midi % 12 not in white_keys:
            scales[i][k].sign = signs['M'][i]
    scales[str(i) + 'M'] = scales[i]

    scales[str(i) + 'm'] = [Pit(j + i) for j in scales['minor']]
    for k in range(0, len(scales[str(i) + 'm'])):
        if scales[str(i) + 'm'][k].midi % 12 not in white_keys:
            scales[str(i) + 'm'][k].sign = signs['m'][i]

seventh_probs = {0: 0,
                 1: 0.1,
                 2: 0.1,
                 3: 0.0,
                 4: 0.4,
                 5: 0,
                 6: 0}
ninth_probs = {0: 0.1,
               1: 0.1,
               2: 0.1,
               3: 0.1,
               4: 0,
               5: 0.0,
               6: 0.1}

inversion_probs = {0: {0: 0.7,
                       1: 0.25,
                       2: 0.05},
                   1: {0: 0.5,
                       1: 0.5},
                   2: {0: 0.7,
                       1: 0.3},
                   3: {0: 0.5,
                       1: 0.3,
                       2: 0.2},
                   4: {0: 0.5,
                       1: 0.3,
                       2: 0.2},
                   5: {0: 0.4,
                       1: 0.6},
                   6: {1: 1.0}}
