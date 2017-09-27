import matplotlib.pyplot as plt

def plot_sample(samples):
    """
    plot_sample: plots the xy tuples on a plane
    :param sample: an array of xy tuples
    :return: None
    """
    if type(samples) != list:
        raise TypeError('"samples" must be of type list.')
        exit(1)
    x_coords = list(map(lambda x: x[0], samples))
    y_coords = list(map(lambda x: x[1], samples))
    plt.plot(x_coords, y_coords, 'k.')
    plt.show()