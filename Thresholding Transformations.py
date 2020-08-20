import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():
    img_name = sys.argv[1]
    img = cv2.cvtColor(cv2.imread(img_name), cv2.COLOR_BGR2RGB)

    # Set the threshold function to be greater than 200, (or less than 200)
    img[img < 210] = 0

    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    main()
