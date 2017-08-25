# -*- coding: utf-8 -*-
# shannon.py
import math


def entropy(string):
    """
    Calculates the Shannon entropy of a string
    :param string:
    :return: shannon entropy value
    """

    # get probability of chars in string
    prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]

    # calculate the entropy
    entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])

    return entropy

e = entropy('correct-horse-battery-staple')
print('The password entropy is {}'.format(e))

