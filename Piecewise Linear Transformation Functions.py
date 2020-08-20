import sys
import cv2
import matplotlib.pyplot as plt


def main():
    img_name = sys.argv[1]
    img = cv2.cvtColor(cv2.imread(img_name), cv2.COLOR_BGR2RGB)

    img = img / 255
    img = 0.5 * img
    img[img < (50/255)] = 2 * img[img < (50/255)]
    img[img > (100/255)] = 2 * img[img > (100/255)]

    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    main()
