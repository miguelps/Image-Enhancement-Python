import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():
    img_name = sys.argv[1]
    img = cv2.cvtColor(cv2.imread(img_name), cv2.COLOR_BGR2RGB)

    c = 1
    r = 0.4

    img_gamma = c * np.power(img/255, r)

    plt.imshow(img_gamma)
    plt.show()


if __name__ == '__main__':
    main()
