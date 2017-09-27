import unittest
from math import sqrt
import Sampling.sample_backend as sample_b


class TestSample(unittest.TestCase):
    """
    Test Suite for testing code in sample_backend.py and
    sample_frontend.py
    """

    def test_distance(self):
        a1 = [0, 0]
        b1 = [3, 4]
        x1 = sample_b.distance(a1,b1)
        self.assertEqual(x1, 5.0, 'Distance from a to b should be 5')
        a2 = [1,2]
        b2 = [34,4]
        x2 = sample_b.distance(a2,b2)
        self.assertEqual(x2, sqrt(33**2 + 2**2))

    def test_findClosest(self):
        samples = [[0,0],[1,1],[2,2],[3,3],[4,4]]
        a1 = [1.1,1.1]
        x1 = sample_b.findClosest(samples, a1)
        self.assertEqual(x1, [1,1])
        a2 = [1,2]
        x2 = sample_b.findClosest(samples, a2)
        self.assertEqual(x2, [1,1])

if __name__ == '__main__':
    unittest.main()