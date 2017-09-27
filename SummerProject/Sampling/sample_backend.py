import sys
from math import sqrt
from random import random

_X_INDEX = 0
_Y_INDEX = 1

def sample_all(size, numCandidates, samples):
    """
    sample_all: calls sample size number of times to create an even
    distribution and updates the sample to proceed
        :param size: the number of points withing the sampling space
        :param numCandidates: the number of samples to take in
            determining where each point should go (the
            higher numCandidates is the higher the quality of
            the sample but the slower the generation speed).
        :param sample: array to use when finding closest point
        :return: an array of xy tuples
    """
    for i in range(0,size):
        samples.append(sample(numCandidates, samples))
    return samples


def sample(numCandidates, samples):
    """
    sample: creates the next point in an evenly distributed approximate
    Poisson-disc distribution. numCandidates = 1 degenerates to a
    purely random sample
        :param numCandidates: the number of samples to take in
            determining where each point should go (the
            higher numCandidates is the higher the quality of
            the sample but the slower the generation speed).
        :param sample: array to use when finding closest point
        :return: an array of size 2 where the 0th index is the x-
            position and the 1st index is the y-position
    """
    if len(samples) == 0:
        return [random(),random()]
    bestCandidate = [None,None]
    bestDistance = 0
    for i in range(0,numCandidates):
        currPt = [random(),random()]
        currDist = distance(findClosest(samples, currPt), currPt)
        if(currDist > bestDistance):
            bestDistance = currDist
            bestCandidate = currPt
    return bestCandidate

def findClosest(samples, point):
    """
    findClosest: find the point from samples that is closest to 'point'
        :param samples: an array where each index is an array where the first
            index is the x-coordinate and the second is the y-
            coordinate
        :param point: an array of size 2 where the 0th index is the x-
            position and the 1st index is the y-position; the point
            that will be used to determine the nearest point
        :return: an array of size 2 where the 0th index is the x-
            position and the 1st index is the y-position
    """
    if len(samples) == 0:
        return point
    bestPoint = [None, None]
    bestDist = sys.maxsize
    for i in range(0, len(samples)):
        currDist = distance(samples[i], point)
        if currDist < bestDist:
            bestDist = currDist
            bestPoint = samples[i]
    return bestPoint


def distance(pointA, pointB):
    """
    distance: calculates the distance from pointA to pointB
        :param pointA: an array of size 2 where the 0th index is the x-
            position and the 1st index is the y-position
        :param pointB: an array of size 2 where the 0th index is the x-
            position and the 1st index is the y-position
        :return: a float representing the distance from pointA to
            pointB
    """
    dx = abs(pointB[_X_INDEX] - pointA[_X_INDEX])
    dy = abs(pointB[_Y_INDEX] - pointA[_Y_INDEX])
    return sqrt(dx**2 + dy**2)