from skimage import io
from functools import reduce
import matplotlib.pyplot as plt

gradient = io.imread('D:\Programming\Python\SummerProject\Image Processing\grey_gradient.jpg')
colorful = io.imread('D:\Programming\Python\SummerProject\Image Processing\colorful.jpg')

io.imshow(gradient)
plt.show()


def average_blur(img):
    """
    average_blur: the average is taken of every other pixel and the
        surrounding 8 pixels and the 9 pixels are made the same shade
        that is the average of all 9 pixels.
    :param img: image to blur
    :return: None
    """
    for x in range(1, img.shape[0] - 1):
        if (x >= img.shape[0]):
            pass
        for y in range(1, img.shape[1] - 1):
            if(y >= img.shape[1]):
                pass
            sum_r = int(img[x - 1, y - 1][0]) + int(img[x, y - 1][0]) + int(img[x + 1, y - 1][0]) + \
                    int(img[x - 1, y][0]) + int(img[x, y][0]) + int(img[x + 1, y][0]) + \
                    int(img[x - 1, y + 1][0]) + int(img[x, y + 1][0]) + int(img[x + 1, y + 1][0])
            sum_g = int(img[x - 1, y - 1][1]) + int(img[x, y - 1][1]) + int(img[x + 1, y - 1][1]) + \
                    int(img[x - 1, y][1]) + int(img[x, y][1]) + int(img[x + 1, y][1]) + \
                    int(img[x - 1, y + 1][1]) + int(img[x, y + 1][1]) + int(img[x + 1, y + 1][1])
            sum_b = int(img[x - 1, y - 1][2]) + int(img[x, y - 1][2]) + int(img[x + 1, y - 1][2]) + \
                    int(img[x - 1, y][2]) + int(img[x, y][2]) + int(img[x + 1, y][2]) + \
                    int(img[x - 1, y + 1][2]) + int(img[x, y + 1][2]) + int(img[x + 1, y + 1][2])
            img[x, y][0] = int(sum_r / 9)
            img[x, y][1] = int(sum_g / 9)
            img[x, y][2] = int(sum_b / 9)
            y += 2
        x += 2
    return img

for i in range(0,10):
    colorful = average_blur(colorful)
    colorful = average_blur(colorful)
    colorful = average_blur(colorful)
    colorful = average_blur(colorful)
    colorful = average_blur(colorful)
    colorful = average_blur(colorful)
    colorful = average_blur(colorful)
    colorful = average_blur(colorful)
    colorful = average_blur(colorful)
    colorful = average_blur(colorful)
    io.imshow(colorful)
    plt.show()