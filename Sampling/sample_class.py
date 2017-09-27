from Sampling.sample_backend import sample_all
from Sampling.sample_frontend import plot_sample

class Sampling:
    """
    Class to encapsulate frontend and backend of sampling program
    """

    def __init__(self, size, numCandidates=1, curr_samples=[]):
        """
        __init__: constructor for Sampling class
            :param numCandidates: the number of random samples to take
                when finding the next best point to add (default 1,
                completely random sampling)
            :param size: the number of points to be within the sample
                space
        """
        self.size = size
        self.numCandidates = numCandidates
        self.samples = None
        self.curr_samples = []
        self.create_sample()

    def show_samples(self):
        """
        show_samples: displays the sample space in cartesian plane
        :return: None
        """
        try:
            plot_sample(self.samples)
        except TypeError:
            pass

    def create_sample(self):
        """
        create_sample: wrapper for sample_all function, sets the value
            returned to self.samples.
            :param curr_samples: if there is a previous sample space,
                will take it into account
            :return: None
        """
        self.samples = sample_all(self.size, self.numCandidates, self.curr_samples)