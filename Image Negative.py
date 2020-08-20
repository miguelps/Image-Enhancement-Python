import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():
    img_name = sys.argv[1]
    img = cv2.cvtColor(cv2.imread(img_name), cv2.COLOR_BGR2RGB)

    img_negative = 256 - img

    plt.imshow(img)
    plt.imshow(img_negative)
    plt.show()


if __name__ == '__main__':
    main()
