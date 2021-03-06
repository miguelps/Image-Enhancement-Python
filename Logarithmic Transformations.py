import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():
    img_name = sys.argv[1]
    img = cv2.cvtColor(cv2.imread(img_name), cv2.COLOR_BGR2RGB)
    c = 1.55
    img_trans = c * np.log(1 + img / 255)
    # print(img_trans.min(), img_trans.max())
    img_trans[img_trans > 1] = 1
    img_trans[img_trans < 0] = 0

    plt.imshow(img_trans)
    plt.show()


if __name__ == '__main__':
    main()
