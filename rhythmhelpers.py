__author__ = 'halley'
import probabilityhelpers as ph
import random
import functionalhelpers as fh
#for checking whether two numbers are roughly the same
def almostEquals(x,y):
    if abs(x - y) < 0.001:
        return True
    return False


def strToRhy(rstr):
    return [float(i) for i in rstr.split()]

def rhyToStr(rhy):
    return ' '.join([str(i) for i in rhy])

def isIDRhythm(durs, beat_durs = None):
    abs_durs = map(abs, durs)
    if abs_durs == [0.5,1.0,0.5] or abs_durs == [0.25,0.25,1.0,0.25, 0.25] or abs_durs == [0.5,1.0,0.25,0.25] or abs_durs == [0.25,0.25,1.0,0.5]:
        return (True, 'sync')
    if -0.25 in durs:
        return (True, 'rest')
    if -0.5 in durs[:-2]:
        return (True, 'rest')
    if any([almostEquals(i, 1.0/6.0) for i in abs_durs]):
        return (True, 'sixtuplets')
    if any([almostEquals(i, 1.0/3.0) for i in abs_durs]):
        return (False, 'triplets')
    if beat_durs[0] == [0.5, 0.25,0.25] or beat_durs[1] == [0.5,0.25,0.25]:
        return (False, 'halving')
    return (False, False)

one_prob_dict = {'1.0':0.3, '-1.0':0.1, '0.75 0.25':0.05, '0.5 0.5':0.2, '0.5 0.25 0.25':0.05, '0.25 0.25 0.5':0.01, '0.25 0.5 0.25':0.01, '-0.5 0.5':0.02, '0.5 -0.25 0.25':0.01, '-0.5 0.5':0.05}
half_prob_dict = {'0.5':0.5, '0.25 0.25':0.1}
one_and_a_half_prob_dict = {'1.5':0.8, '0.5 1.0':0.2, '1.25 0.25':0.05, '-0.5 1.0':0.02}
two_prob_dict = {}
two_prob_dict['2.0'] = 0.2

#create probability dict for two beats
for first_val, first_prob in one_prob_dict.items():
    for second_val, second_prob in one_prob_dict.items():
        if not ('-' in first_val and '-' in second_val): #if they don't both have rests
            two_prob_dict[first_val + ' ' + second_val] = first_prob * second_prob
for one_and_a_half_val, one_and_a_half_prob in one_and_a_half_prob_dict.items():
    for half_prob_val, half_prob in half_prob_dict.items():
        two_prob_dict[one_and_a_half_val + ' ' + half_prob_val] = one_and_a_half_prob * half_prob * 0.1

#return a random duration
def randomDuration(length = 2.0, same = '', avoid = []):
    if length == 2.0:
        new_prob_dict = {}
        for val, prob in two_prob_dict.items():
            if val not in avoid:
                new_prob_dict[val] = prob
        return strToRhy(ph.probDictToChoice(new_prob_dict))
    elif length == 4.0:
        if same == '':
            same = random.choice([True, False])
        if same:
            a = notHalfNote()
            return fh.concat([a,a])
        else:
            if random.uniform(0,1) < 0.1 and '3.0 1.0' not in avoid and '3.0 0.5 0.5' not in avoid and '1.0 2.0 1.0' not in avoid:
                a = strToRhy(ph.probDictToChoice({'3.0 1.0':0.2, '3.0 0.5 0.5':0.4, '1.0 2.0 1.0': 0.6}))
                return a
            else:
                return randomDuration(2.0, avoid=avoid) + randomDuration(2.0, avoid=avoid)

def notHalfNote():
    return randomDuration(length = 2.0, avoid = ['2.0'])


def alterRhythm(cell):
    new_durs = []
    simple = [[1.0], [0.5,0.5],[0.25,0.25,0.25,0.25],[0.5,0.5]]
    beat_durs = cell.beat_durs
    if len(beat_durs) == 1:
        return cell.durs
    else:
        if random.uniform(0,1) < 0.5 or beat_durs[1] not in simple:
            simple_other = filter(lambda i: i != beat_durs[0], simple)
            new_durs.extend(random.choice(simple_other))
            new_durs.extend(beat_durs[1])
        else:
            new_durs.extend(beat_durs[0])
            simple_other = filter(lambda i: i != beat_durs[1], simple)
            new_durs.extend(random.choice(simple_other))
    return new_durs




