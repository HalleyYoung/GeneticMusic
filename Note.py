__author__ = 'halley'
from constants import *

class Note():
    def __init__(self, pit=None, dur=0, midi=None, scale=None, degree=None, sign=0):
        self.pit = pit
        self.dur = dur
        self.midi = midi
        self.scale = scale
        self.degree = degree
        self.sign = sign

        if self.pit is None and self.scale is not None and self.degree is not None:
            scale = scales[self.scale]
            sign = 0 if self.sign is None else self.sign
            self.midi = scale[degree % len(scale)].midi + (degree/len(scale)) * 12 + sign
            self.pit = Pit(midi=self.midi, scale=self.scale, degree=self.degree, sign=self.sign)

def pitToPitch(scale_note):
    if scale_note.midi != None and scale_note.midi % 12 in white_keys:
        return scale_note.midi
    else:
        degree = scale_note.degree
        scale = scale_note.scale
        scale_root = int(scale[:-1])
        scale_type = scale[-1]
        scale_sign = signs[scale_type][scale_root]
        natural_is_signed = (scales[scale][degree % 7].midi ) % 12 not in white_keys
        if natural_is_signed:
            sign = scale_sign + scale_note.sign
        else:
            sign = scale_note.sign
        note_choices = notes[scale_note.midi]
        if sign == -2:
            pitch_name = filter(lambda i: i.count('-') == 2, note_choices)[0]
        elif sign == -1:
            pitch_name = filter(lambda i: i.count('-') == 1, note_choices)[0]
        elif sign == 0:
            pitch_name = filter(lambda i: i.count('-') == 0 and i.count('#') == 0, note_choices)[0]
        elif sign == 1:
            pitch_name = filter(lambda i: i.count('#') == 1, note_choices)[0]
        elif sign == 2:
            pitch_name = filter(lambda i: i.count('#') == 2, note_choices)[0]
        return pitch_name
