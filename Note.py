__author__ = 'halley'
from constants import *

class Note():
    def __init__(self, pit = None, dur = 0, midi = None, scale = None, degree = None, sign = 0):
        if pit != None:
              self.pit = pit
              self.scale = pit.scale
              self.degree = pit.degree
              self.sign = pit.sign
              self.midi = pit.midi
              self.dur = dur
        elif pit == None and self.scale != None and self.degree != None:
            self.scale = scale
            self.degree = degree
            self.sign = sign
            scale = scales[self.scale]
            sign = 0 if self.sign == None else self.sign
            self.midi = scale[degree % len(scale)].midi + (degree/len(scale)) * 12 + sign
            self.pit = Pit(midi=self.midi, scale = self.scale, degree = self.degree, sign = self.sign)
            self.dur = dur
        else:
            self.midi = midi
            self.dur = dur