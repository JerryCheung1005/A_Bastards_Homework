from itertools import groupby
import matplotlib.pyplot as plt
import random

c = []
d = []
for i in range(24):
    c.append(random.randint(0, 101))
    d.append(random.randint(0, 101))
scores = {
    'data structure': [89, 70, 49, 87, 92, 84, 73, 71, 78, 81, 90, 37, 77, 82, 81, 79, 80, 82, 75, 90, 54, 80, 70, 68,
                       61],
    'linear regression': [70, 74, 80, 60, 50, 87, 68, 77, 95, 80, 79, 74, 69, 64, 82, 81, 78, 90, 78, 79, 72, 69, 45,
                          70, 70],
    'English': c,
    'Python': d}


def splitScore(score):
    if score >= 85:
        return 'Distinction'
    elif 60 < score < 85:
        return 'Pass'
    else:
        return 'Fail'


